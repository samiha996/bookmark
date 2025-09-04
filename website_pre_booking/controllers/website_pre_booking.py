# -*- coding: utf-8 -*-
from odoo import fields, http, _
from odoo.http import request


class CustomerPortal(http.Controller):
    """Used to manage a customer portal"""

    @http.route(['/my/prebook_request/<model("product.template"):product>'],
                type='http', auth="public", website=True)
    def portal_my_employee_request(self, product, **kwargs):
        """Pre-book button to pre-book the product"""
        # --- Defensive parse for quantity ---
        raw_qty = kwargs.get('prod_qty')
        try:
            # Accept floats but store as int; default to 1 if missing/invalid
            product_qty = int(float(raw_qty)) if raw_qty not in (None, "",) else 1
        except Exception:
            product_qty = 1
        if product_qty < 1:
            product_qty = 1

        # Validate available pre-book quantity if configured
        max_quantity = int(product.pre_max_quantity or 0)
        if max_quantity and product_qty > max_quantity:
            # Exceeds allowed quantity: show fail page
            return request.render("website_pre_booking.pre_booking_failed")

        vals = {'product': product.id, 'prod_qty': product_qty}

        # Logged-in user flow
        if request.session.uid:
            current_user = request.env['res.users'].sudo().browse(request.session.uid)
            partner = current_user.partner_id

            pre_booking = request.env['website.prebook'].sudo().create({
                'partner_id': partner.id,
                'booking_date': fields.Date.today(),
                'product_id': product.id,
                'quantity': product_qty,
                'website_id': request.website.id,
            })
            if pre_booking and max_quantity:
                product.sudo().write({'pre_max_quantity': max_quantity - product_qty})

            return request.render("website_pre_booking.pre_booking_done",
                                  {'ref': pre_booking.reference})
        # Public (not logged in): send to address form and keep qty
        else:
            return request.render("website_pre_booking.prebook_address", vals)

    @http.route(['/prebook/address'], type='http', methods=['GET', 'POST'],
                auth="public", website=True, sitemap=False)
    def pre_address(self, **kw):
        """If not login, create a new partner and pre-book with provided qty"""
        # Defensive read for product and quantity
        product_id = int(kw.get('product') or 0)
        product = request.env['product.template'].sudo().browse(product_id)
        raw_qty = kw.get('prod_qty')
        try:
            qty = int(float(raw_qty)) if raw_qty not in (None, "",) else 1
        except Exception:
            qty = 1
        if qty < 1:
            qty = 1

        # Validate against max quantity
        max_quantity = int(product.pre_max_quantity or 0)
        if max_quantity and qty > max_quantity:
            return request.render("website_pre_booking.pre_booking_failed")

        partner = request.env['res.partner'].sudo().create({
            'name': kw.get('name'),
            'email': kw.get('email'),
            'phone': kw.get('phone'),
        })

        pre_booking = request.env['website.prebook'].sudo().create({
            'partner_id': partner.id,
            'booking_date': fields.Date.today(),
            'product_id': product.id,
            'quantity': qty,
            'website_id': request.website.id,
        })
        if pre_booking and max_quantity:
            product.sudo().write({'pre_max_quantity': max_quantity - qty})

        return request.render("website_pre_booking.pre_booking_done",
                              {'ref': pre_booking.reference})

    @http.route('/track/prebooking', website=True, auth='user', csrf=False)
    def submit_booking(self, **kwargs):
        """For tracking the specific pre-orders using reference code"""
        bookings = request.env['website.prebook'].sudo().search(
            [('reference', '=', kwargs.get('reference'))])
        if bookings and bookings.sale_id:
            if bookings.sale_id.state == 'draft':
                state = 'Quotation'
            elif bookings.sale_id.state == 'sent':
                state = 'Quotation Sent'
            elif bookings.sale_id.state == 'sale':
                state = 'Sales Order'
            elif bookings.sale_id.state == 'done':
                state = 'Locked'
            elif bookings.sale_id.state == 'cancel':
                state = 'Cancelled'
            vals = {
                'reference': bookings.reference,
                'product': bookings.product_id.name,
                'status': state if bookings.sale_id else bookings.state,
                'date': bookings.booking_date,
            }
            return request.render("website_pre_booking.my_booking_template", vals)
        else:
            return request.render("website_pre_booking.my_booking_template", {'vals': True})

    @http.route(['/my/prebookings', '/my/prebookings/page/<int:page>'],
                type='http', auth="user", website=True)
    def my_prebookings(self):
        """Can track the pre bookings from the website"""
        value = []
        values = {'value': value}
        return request.render("website_pre_booking.my_booking_template", values)

    @http.route(['/sale/fail'], type='http', auth="user", website=True)
    def my_prebookings_fail(self):
        """Failure page"""
        return request.render("website_pre_booking.pre_booking_failed")
