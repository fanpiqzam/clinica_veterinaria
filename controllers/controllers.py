# -*- coding: utf-8 -*-
from odoo import http

# class ClinicaVeterinaria(http.Controller):
#     @http.route('/clinica_veterinaria/clinica_veterinaria/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/clinica_veterinaria/clinica_veterinaria/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('clinica_veterinaria.listing', {
#             'root': '/clinica_veterinaria/clinica_veterinaria',
#             'objects': http.request.env['clinica_veterinaria.clinica_veterinaria'].search([]),
#         })

#     @http.route('/clinica_veterinaria/clinica_veterinaria/objects/<model("clinica_veterinaria.clinica_veterinaria"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('clinica_veterinaria.object', {
#             'object': obj
#         })