from odoo import models, fields, api

class ProductTemplate(models.Model):
    _inherit = 'product.template'

    department_id = fields.Many2one('department', string='Department')
    serie_id = fields.Many2one('serie', string='Serie')
    school_id = fields.Many2one('product.school', string="School")
    author_id = fields.Many2one('book.author', string="Author")
    author2_id = fields.Many2one('book.author', string="Author 2")
    
