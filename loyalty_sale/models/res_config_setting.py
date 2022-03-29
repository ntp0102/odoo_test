# -*- coding: utf-8 -*-


from odoo import models, fields, api


class ResConfigSetting(models.TransientModel):
    _inherit = 'res.config.settings'


    loyalty_for_sale_id = fields.Many2one(comodel_name='program',string='Danh sách chương trình đang khuyến mãi')