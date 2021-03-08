# -*- coding: utf-8 -*-

from odoo import models, fields, api
from odoo import modules
import base64
from odoo.exceptions import ValidationError
import datetime
import re
import requests
import logging
import base64

class veterinario_model(models.Model):
    
    _name = "clinica_veterinaria.vet_model"
    _order = 'apellidos'
    _sql_constraints = [
        ('vet_nombre_unique','UNIQUE(name)','No puede haber dos veterinarios con el mismo DNI!'),
    ]

    name = fields.Char('DNI', required=True)
    nombre = fields.Char('Nombre', required=True)
    apellidos = fields.Char('Apellidos')
    foto = fields.Binary('Foto')
    telefono = fields.Char('Telefono')
    email = fields.Char('Email')
    atienden = fields.One2many('clinica_veterinaria.atienden_model','veterinario')
    clinica = fields.Many2one('clinica_veterinaria.clinica_model')


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

    @api.one
    @api.constrains('email')
    def _check_email(self):
        if not re.match(r"[^@]+@[^@]+\.[^@]+", self.email):
            raise ValidationError("Email no válido.")