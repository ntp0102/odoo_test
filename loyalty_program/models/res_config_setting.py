# -*- coding: utf-8 -*-


from odoo import models, fields, api


class ResConfigSetting(models.TransientModel):
    _inherit = 'res.config.settings'

    loyalty_email_notify = fields.Boolean(string='Phản hồi Email', default=False)