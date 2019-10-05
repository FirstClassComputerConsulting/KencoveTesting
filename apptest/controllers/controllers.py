# -*- coding: utf-8 -*-
from odoo import http

# class Apptest(http.Controller):
#     @http.route('/apptest/apptest/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/apptest/apptest/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('apptest.listing', {
#             'root': '/apptest/apptest',
#             'objects': http.request.env['apptest.apptest'].search([]),
#         })

#     @http.route('/apptest/apptest/objects/<model("apptest.apptest"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('apptest.object', {
#             'object': obj
#         })