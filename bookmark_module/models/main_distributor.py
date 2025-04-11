from odoo import models, fields

class MainDistributor(models.Model):
    _name = 'main.distributor'
    _description = 'Main Distributor'

    name = fields.Char(string="Main Distributor", required=True)
