from odoo import models, fields, api


class Serie(models.Model):
    _name = 'serie'
    _description = 'Serie'

    name = fields.Text(string='Name', required=True)
    product_ids = fields.One2many('product.product', 'serie_id', string='Products')
    product_count = fields.Integer(string='Product Count', compute='_compute_product_count')

    @api.depends('product_ids')
    def _compute_product_count(self):
        for serie in self:
            serie.product_count = len(serie.product_ids)