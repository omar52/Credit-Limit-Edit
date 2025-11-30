from odoo import models, fields, api


class ResPartner(models.Model):
    _inherit = 'res.partner'

    region_id = fields.Many2one('res.region', string='Region')
