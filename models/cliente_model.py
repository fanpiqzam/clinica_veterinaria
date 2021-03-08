# -*- coding: utf-8 -*-

from odoo import models, fields, api
from odoo.exceptions import ValidationError
import datetime
import re

class cliente_model(models.Model):
    _name = "clinica_veterinaria.cliente_model"
    _order = 'apellidos'
    _sql_constraints = [
        ('dni_cliente_unico','UNIQUE(name)','No puede haber dos clientes con el mismo DNI!'),
    ]

    name = fields.Char('DNI', required=True)
    nombre = fields.Char('Nombre', required=True)
    apellidos = fields.Char('Apellidos')
    telefono = fields.Char('Telefono', required=True)
    email = fields.Char('Email')
    mascota = fields.One2many('clinica_veterinaria.mascota_model','cliente')
    factura = fields.One2many('clinica_veterinaria.factura_model','cliente',ondelete='cascade')
    historial = fields.One2many('clinica_veterinaria.historial_model','cliente')

    @api.one
    @api.constrains('telefono')
    def _checkTelf(self):
        telf = self.telefono
        if (len(telf)<9 or len(telf)>9):
            raise ValidationError("El teléfono ha de tener 9 números.")
        elif (telf.isalpha()):
            raise ValidationError("El teléfono no puede contener letras.")

    @api.one
    @api.constrains('name')
    def _check_dni(self):
        letras = ["T","R","W","A","G","M","Y","F","P","D","X","B","N","J","Z","S","Q","V","H","L","C","K","E"]
        
        letraDNI = self.name[-1].upper()
        numDNI = self.name[:-1]

        if (letraDNI.isalpha() == False):
            raise ValidationError("DNI incorrecto. DNI son 8 números más una letra.")
        if len(self.name) != 9:
            raise ValidationError("La longitud del DNI es incorrecta!")
        else:
            letraCalculada = letras[int(numDNI)%23]
            if (letraDNI != letraCalculada):
                raise ValidationError("El DNI no es válido.")
        return True

    @api.one
    @api.constrains('email')
    def _check_email(self):
        if not re.match(r"[^@]+@[^@]+\.[^@]+", self.email):
            raise ValidationError("Email no válido.")