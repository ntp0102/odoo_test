# -*- coding: utf-8 -*-

from odoo import models, fields, api


class LoyaltySale(models.Model):
    # _name = 'loyalty.sale'
    _inherit = 'sale.order'

    program = fields.Many2one(comodel_name='program')
    partner_id = fields.Many2one(comodel_name='res.partner', string='Customer')
    loyalty_points_accumulated = fields.Float(related='partner_id.accumulated_points')
    loyalty_points_accumulating = fields.Float(string='Tổng số điểm tích lũy nhận được trong đơn hàng',
                                               compute='_get_points')
    loyalty_points_won = fields.Float('Tổng điểm tích lũy', compute='_get_points')
    _points = fields.Float(related='program.points')


    @api.depends('program','amount_untaxed')
    def _get_points(self):
        for rec in self:
            rec.loyalty_points_accumulating = float(rec.amount_untaxed) * float(rec._points) / 100
            rec.loyalty_points_won = float(rec.loyalty_points_accumulated) + float(rec.loyalty_points_accumulating)

    def action_confirm(self):
        vals1 = {
            'accumulated_points': self.loyalty_points_won
        }
        self.env['res.partner'].browse(self.partner_id.ids[0]).write(vals1)

        vals2 = {
            'name': self.name,
            'customer_id': self.partner_id.name,
            'money_spent': float(self.amount_total),
            'loyalty_points': self.loyalty_points_accumulating,
            'loyalty_point': self.loyalty_points_won,
            'partner_id': self.program.name
        }
        self.env['history'].create(vals2)
        # print('Hello bro')
        # print(vals)
        # print(rec.partner_id)
        # print(rec.state)

        res = super(LoyaltySale, self).action_confirm()
        return True

    def action_cancel(self):
        vals1 = {
            'accumulated_points': self.loyalty_points_accumulated - self.loyalty_points_accumulating
        }
        self.env['res.partner'].browse(self.partner_id.ids[0]).write(vals1)

        vals2 = {
            'name': self.name,
            'customer_id': self.partner_id.name,
            'money_spent': - float(self.amount_total),
            'loyalty_points': - self.loyalty_points_accumulating,
            'loyalty_point': self.loyalty_points_accumulated,
            'partner_id': self.program.name
        }
        self.env['history'].create(vals2)

        res = super(LoyaltySale, self).action_cancel()
        return True

