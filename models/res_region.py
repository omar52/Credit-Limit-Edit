from odoo import models, fields

class ResRegion(models.Model):
    _name = 'res.region'

    region_name = fields.Char()
    region_code = fields.Char()
