from odoo import models, fields, api

class ProductTemplate(models.Model):
    _inherit = 'product.template'

    department_id = fields.Many2one('department', string='Department')
    serie_id = fields.Many2one('serie', string='Serie')
    school_id = fields.Many2one('product.school', string="School")
    author_id = fields.Many2one('book.author', string="Author")
    author2_id = fields.Many2one('book.author', string="Author 2")
    title2 = fields.Char(string="Title 2")
    subtitle = fields.Char(string="Subtitle")
    subtitle2 = fields.Char(string="Subtitle 2")
    date_of_publication = fields.Date(string="Date of Publication")
    publisher = fields.Many2one('publisher', string="Publisher")
    main_distributor = fields.Many2one('main.distributor', string="Main Distributor")
    
