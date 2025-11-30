from email.policy import default

from odoo import models, fields, api


class ResPartner(models.Model):
    _inherit = 'res.partner'

    region_id = fields.Many2one('res.region', string='Region')

    credit_limit = fields.Float(
        string="Credit Limit",
        compute='_compute_credit_limit',
        store=True
    )
    is_credit_limit_disabled = fields.Boolean(
        string="Is Credit Limit Disabled",
        compute='_compute_credit_limit',
        store=True
    )

    @api.depends('credit_limit')
    def _compute_credit_limit(self):
        config_value = self.env['ir.config_parameter'].sudo().get_param('sales.enable_credit_limit')
        floated_value = float(config_value) if config_value else 0.0

        for partner in self:
            if partner.is_credit_limit_disabled:
                partner.credit_limit = floated_value
                partner.is_credit_limit_disabled = False
            else:
                partner.credit_limit = floated_value
                partner.is_credit_limit_disabled = True

