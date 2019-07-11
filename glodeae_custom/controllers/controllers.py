# -*- coding: utf-8 -*-
from odoo import http

# class GlodeaeCustom(http.Controller):
#     @http.route('/glodeae_custom/glodeae_custom/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/glodeae_custom/glodeae_custom/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('glodeae_custom.listing', {
#             'root': '/glodeae_custom/glodeae_custom',
#             'objects': http.request.env['glodeae_custom.glodeae_custom'].search([]),
#         })

#     @http.route('/glodeae_custom/glodeae_custom/objects/<model("glodeae_custom.glodeae_custom"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('glodeae_custom.object', {
#             'object': obj
#         })