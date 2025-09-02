# -*- coding: utf-8 -*-
from odoo import api, fields, models
from odoo.tools.float_utils import float_round

class PurchaseOrderLine(models.Model):
    _inherit = 'purchase.order.line'
    
    barcode = fields.Char(
        string='Barcode',
        related='product_id.barcode',
        store=True,
        readonly=True
    )
    product_internal_reference = fields.Char(
        string="Internal Reference",
        related='product_id.default_code',
        readonly=True,
        store=False
    )

    # Your new field
    extra_discount = fields.Float(string="Disc. 2 (%)", digits='Discount', default=0.0)

    # Helper: multiplicative combination of both discounts
    def _get_effective_discount(self):
        self.ensure_one()
        d1 = (self.discount or 0.0) / 100.0
        d2 = (self.extra_discount or 0.0) / 100.0
        eff = 1.0 - ((1.0 - d1) * (1.0 - d2))
        return eff * 100.0  # back to %
    
    # Ensure totals recompute when Discount 2 changes
    @api.depends('product_qty', 'price_unit', 'taxes_id', 'discount', 'extra_discount')
    def _compute_amount(self):
        for line in self:
            # re-use the same engine but with our effective discount
            tax_results = line.env['account.tax']._compute_taxes([
                line._convert_to_tax_base_line_dict()
            ])
            totals = next(iter(tax_results['totals'].values()))
            amount_untaxed = totals['amount_untaxed']
            amount_tax = totals['amount_tax']
            line.update({
                'price_subtotal': amount_untaxed,
                'price_tax': amount_tax,
                'price_total': amount_untaxed + amount_tax,
            })

    # Inject the effective discount into the tax base dict
    def _convert_to_tax_base_line_dict(self):
        self.ensure_one()
        base = super()._convert_to_tax_base_line_dict()
        base['discount'] = self._get_effective_discount()
        return base

    # Keep the “Unit Price (Discounted)” widget accurate
    @api.depends('discount', 'extra_discount', 'price_unit')
    def _compute_price_unit_discounted(self):
        for line in self:
            eff = (1 - ((1 - (line.discount or 0.0)/100.0) * (1 - (line.extra_discount or 0.0)/100.0)))
            line.price_unit_discounted = float_round(
                line.price_unit * (1 - eff),
                precision_digits=max(line.currency_id.decimal_places, line.env['decimal.precision'].precision_get('Product Price'))
            )

    # Make vendor bills show the combined discount too
    def _prepare_account_move_line(self, move=False):
        vals = super()._prepare_account_move_line(move=move)
        # Pass the effective (combined) discount to the bill line
        if not self.display_type:
            vals['discount'] = self._get_effective_discount()
        return vals
