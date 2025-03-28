from odoo import models, fields, api

class ProductProduct(models.Model):
    _inherit = 'product.product'

    department_id = fields.Many2one(
        'department',
        string='Department',
        related='product_tmpl_id.department_id',
        store=True,
        readonly=False
    )

    serie_id = fields.Many2one(
        'serie',
        string='Serie',
        related='product_tmpl_id.serie_id',
        store=True,
        readonly=False
    )
    x_publisher = fields.Text(
        related='product_tmpl_id.x_Publisher',
        store=True,
        readonly=False
    )
    x_main_supplier = fields.Text(
        related='product_tmpl_id.x_Main_Supplier',
        store=True,
        readonly=False
    )
    x_authors = fields.Text(
        related='product_tmpl_id.x_Authors',
        store=True,
        readonly=False
    )
    school_id = fields.Many2one(
        'product.school',
        string='School',
        related='product_template_id.school_id',
        store=True,
        readonly=False
    )
