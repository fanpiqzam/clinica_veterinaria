# -*- coding: utf-8 -*-

from odoo import models, fields, api

class servicios_model(models.Model):
    _name = 'clinica_veterinaria.servicios_model'

    name = fields.Char('Nombre', required=True)
    descripcion = fields.Html('Descripción')
    gravedad = fields.Selection([("Bajo","Bajo"),("Medio","Medio"),("Alto","Alto")])
    precio = fields.Float('Precio', required=True)
    detalle = fields.One2many('clinica_veterinaria.detallefac_model','servicio')
    atienden = fields.One2many('clinica_veterinaria.atienden_model','servicio')