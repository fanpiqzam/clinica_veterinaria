# -*- coding: utf-8 -*-

from odoo import models, fields, api

class detallefac_model(models.Model):
    _name = 'clinica_veterinaria.detallefac_model'

    factura = fields.Many2one('clinica_veterinaria.factura_model')
    servicio = fields.Many2one('clinica_veterinaria.servicios_model')
    cantidad = fields.Float('Cantidad')