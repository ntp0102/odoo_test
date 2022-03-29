# -*- coding: utf-8 -*-
# from odoo import http


# class LoyaltySale(http.Controller):
#     @http.route('/loyalty_sale/loyalty_sale', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/loyalty_sale/loyalty_sale/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('loyalty_sale.listing', {
#             'root': '/loyalty_sale/loyalty_sale',
#             'objects': http.request.env['loyalty_sale.loyalty_sale'].search([]),
#         })

#     @http.route('/loyalty_sale/loyalty_sale/objects/<model("loyalty_sale.loyalty_sale"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('loyalty_sale.object', {
#             'object': obj
#         })
