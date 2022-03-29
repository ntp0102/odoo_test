# -*- coding: utf-8 -*-


from odoo import models, fields, api


class LoyaltyHistory(models.Model):
    _name = 'history'
    _description = 'Loyalty History'

    name = fields.Char('Mã đơn hàng')

    partner_id = fields.Char(string='Tên chương trình khuyến mãi')
    loyalty_points = fields.Float(string='Tổng số điểm tích lũy nhận được trong 1 đơn hàng')
    money_spent = fields.Float('Tổng tiền của đơn hàng')
    loyalty_point = fields.Float('Số điểm đã tích lũy của khách hàng')
    date_order = fields.Datetime(string='Thời gian xác nhận đơn hàng', required=True, readonly=True, copy=False,
                                 default=fields.Datetime.now)
    customer_id = fields.Char(string='Tên khách hàng')

    def _employee_get(self):
        return self.env['res.partner'].search([('user_id', '=', uid)], limit=1)



