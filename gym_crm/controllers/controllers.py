# -*- coding: utf-8 -*-
from odoo import http

# class NouveauModule(http.Controller):
#     @http.route('/nouveau_module/nouveau_module/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/nouveau_module/nouveau_module/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('nouveau_module.listing', {
#             'root': '/nouveau_module/nouveau_module',
#             'objects': http.request.env['nouveau_module.nouveau_module'].search([]),
#         })

#     @http.route('/nouveau_module/nouveau_module/objects/<model("nouveau_module.nouveau_module"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('nouveau_module.object', {
#             'object': obj
#         })