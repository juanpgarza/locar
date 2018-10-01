# -*- coding: utf-8 -*-
from odoo import http

# class Locar(http.Controller):
#     @http.route('/locar/locar/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/locar/locar/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('locar.listing', {
#             'root': '/locar/locar',
#             'objects': http.request.env['locar.locar'].search([]),
#         })

#     @http.route('/locar/locar/objects/<model("locar.locar"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('locar.object', {
#             'object': obj
#         })