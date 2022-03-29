# -*- coding: utf-8 -*-
from odoo import models, fields, api


class LoyaltyProgram(models.Model):
    _name = 'program'
    _description = 'Loyalty Program'

    name = fields.Char("Tên chương trình khuyến mãi", required=True)
    points = fields.Float("Số % point nhận được trên 1 đơn hàng", required=True)
    active_program = fields.Boolean(string='Đang hoạt động', required=True, default=False)

    # @api.onchange('active_program')
    # def _check_active(self):
    #     for rec in self:
    #         if rec.active_program:
    #             vals= {
    #                 'program_name': rec.name,
    #                 'date_oder': fields.Datetime.now()
    #             }
    #             self.env['history'].create(vals)
    #         else:
    #             print('hg')
