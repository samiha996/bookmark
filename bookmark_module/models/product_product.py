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
    bookmark_type = fields.Char(
        string='Type',
        related='product_tmpl_id.bookmark_type',
        store=True,
        readonly=False
    )
    url = fields.Char(
        string='Url',
        related='product_tmpl_id.subtitle2',
        store=True,
        readonly=False
    )
    format_size = fields.Char(
        string='Format Size',
        related='product_tmpl_id.format_size',
        store=True,
        readonly=False
    )
    number_page = fields.Integer(
        string='Number of Pages',
        related='product_tmpl_id.number_page',
        store=True,
        readonly=False
    )
    
    bookmark_description = fields.Text(
        string='Description',
        related='product_tmpl_id.bookmark_description',
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
    publisher = fields.Many2one(
        'publisher',
        string='Publisher',
        related='product_tmpl_id.publisher',
        store=True,
        readonly=False
    )
    main_distributor = fields.Many2one(
        'main.distributor',
        string='Main Distributor',
        related='product_tmpl_id.main_distributor',
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
