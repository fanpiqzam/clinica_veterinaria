# -*- coding: utf-8 -*-

from odoo import models, fields, api

class atienden_model(models.Model):
    _name = 'clinica_veterinaria.atienden_model'

    veterinario = fields.Many2one('clinica_veterinaria.vet_model')
    mascota = fields.Many2one('clinica_veterinaria.mascota_model')
    servicio = fields.Many2one('clinica_veterinaria.servicios_model')