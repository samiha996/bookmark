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
    title2 = fields.Char(
        string='Title 2',
        related='product_tmpl_id.title2',
        store=True,
        readonly=False
    )
    subtitle = fields.Char(
        string='Subtitle',
        related='product_tmpl_id.subtitle',
        store=True,
        readonly=False
    )
    subtitle2 = fields.Char(
        string='Subtitle 2',
        related='product_tmpl_id.subtitle2',
        store=True,
        readonly=False
    )
    date_of_publication = fields.Date(
        string='Date of Publication',
        related='product_tmpl_id.date_of_publication',
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
    author_id = fields.Many2one(
        'book.author',
        string='Author',
        related='product_tmpl_id.author_id',
        store=True,
        readonly=False
    )
    author2_id = fields.Many2one(
        'book.author',
        string='Author 2',
        related='product_tmpl_id.author2_id',
        store=True,
        readonly=False
    )
    # school_id = fields.Many2one(
    #     'product.school',
    #     string='School',
    #     related='product_tmpl_id.school_id',
    #     store=True,
    #     readonly=False
    # )
