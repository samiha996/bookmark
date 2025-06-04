from odoo import models, fields, api

class ProductTemplate(models.Model):
    _inherit = 'product.template'

    department_id = fields.Many2one('department', string='Department')
    serie_id = fields.Many2one('serie', string='Serie')
    school_id = fields.Many2one('product.school', string="School")
    author_id = fields.Many2one('book.author', string="Author")
    author2_id = fields.Many2one('book.author', string="Author 2")
    keyword_ids = fields.Many2many(
        comodel_name="product.keyword",
        relation="product_template_keyword_rel",
        column1="product_template_id", 
        column2="keyword_id",           
        string="Keywords",
    )
    title2 = fields.Char(string="Title 2")
    subtitle = fields.Char(string="Subtitle")
    subtitle2 = fields.Char(string="Subtitle 2")
    date_of_publication = fields.Date(string="Date of Publication")
    publisher = fields.Many2one('publisher', string="Publisher")
    main_distributor = fields.Many2one('main.distributor', string="Main Distributor")
    bookmark_type= fields.Char(string="Type")
    url= fields.Char(string="Url")
    bookmark_description = fields.Text(string="Description")
    format_size= fields.Char(string="Format Size")
    number_page= fields.Integer(string="Number of Pages")
    
