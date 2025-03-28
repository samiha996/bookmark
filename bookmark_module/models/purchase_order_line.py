from odoo import models, fields

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
