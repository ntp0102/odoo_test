# -*- coding: utf-8 -*-


from odoo import models, fields, api


class LoyaltyCustomer(models.Model):
    _description = 'Loyalty Customer'
    _inherit = 'res.partner'

    accumulated_points = fields.Float('Số điểm đã tích lũy của khách hàng', readonly=True)
    loyalty_level = fields.Char(string='Cấp độ thân thiết của khách hàng', readonly=True,compute='_level_customer')

    @api.depends('accumulated_points')
    def _level_customer(self):
        for rec in self:
            if (rec.accumulated_points < 1000):
                rec.loyalty_level = 'Đồng'
            elif (rec.accumulated_points < 5000):
                rec.loyalty_level = 'Bạc'
            elif (rec.accumulated_points < 20000 ):
                rec.loyalty_level = 'Vàng'
            else:
                rec.loyalty_level = 'Bạch Kim'

