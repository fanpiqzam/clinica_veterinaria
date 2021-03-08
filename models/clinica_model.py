# -*- coding: utf-8 -*-

from odoo import models, fields, api
from odoo.exceptions import ValidationError
import datetime
import re

class clinica_model(models.Model):
    _name = 'clinica_veterinaria.clinica_model'
    _inherit = ['mail.thread']

    name = fields.Char('Nombre', required=True)
    direccion = fields.Char('Direccion', required=True)
    localidad = fields.Char('Localidad', required=True)
    telefono = fields.Char('Telefono')
    email = fields.Char('Email')
    vet = fields.One2many('clinica_veterinaria.vet_model','clinica',ondelete='cascade')

    @api.one
    @api.constrains('telefono')
    def _checkTelf(self):
        telf = self.telefono
        if (len(telf)<9 or len(telf)>9):
            raise ValidationError("El teléfono ha de tener 9 números.")
        elif (telf.isalpha()):
            raise ValidationError("El teléfono no puede contener letras.")

    @api.one
    @api.constrains('email')
    def _check_email(self):
        if not re.match(r"[^@]+@[^@]+\.[^@]+", self.email):
            raise ValidationError("Email no válido.")
        return True
