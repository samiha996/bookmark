from odoo import models, fields, api

class Department(models.Model):
    _name = 'department'
    _description = 'Department'

    name = fields.Text(string='Name', required=True)
    product_ids = fields.One2many('product.product', 'department_id', string='Products')
    product_count = fields.Integer(string='Product Count', compute='_compute_product_count')

    @api.depends('product_ids')
    def _compute_product_count(self):
        for department in self:
            department.product_count = len(department.product_ids)