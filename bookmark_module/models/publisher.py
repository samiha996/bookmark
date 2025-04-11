from odoo import models, fields

class Publisher(models.Model):
    _name = 'publisher'
    _description = 'Publisher'

    name = fields.Char(string="Publisher", required=True)
