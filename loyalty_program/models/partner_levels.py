# -*- coding: utf-8 -*-


from odoo import models, fields, api


class PartnerLevels(models.Model):
    _name = 'partner.levels'
    _description = 'Partner Levels'

    name = fields.Char('Tên cấp độ', required=True)
    loyalty_points = fields.Float('Số điểm cần đạt được cấp độ tương ứng',required=True)
    description = fields.Text('Mô tả cấp độ')