# -*- coding: utf-8 -*-

from odoo import models, fields, api
from datetime import datetime
from odoo.exceptions import ValidationError

class historial_model(models.Model):
    _name = 'clinica_veterinaria.historial_model'

    name = fields.Char('Nombre', default=lambda self:self._generaId())
    fecha = fields.Datetime('Fecha', required=True, default=datetime.now())
    motivo = fields.Html('Motivo visita', required=True)
    mascota = fields.Many2one('clinica_veterinaria.mascota_model')
    cliente = fields.Many2one('clinica_veterinaria.cliente_model')
    visitaCancelada = fields.Boolean('¿Visita cancelada?', default=False)

    @api.model
    def _generaId(self):
        #lastId = self.env['clinica_veterinaria.factura_model'].search([], order='id desc')[0].id
        if len(self.env['clinica_veterinaria.historial_model'].search([], order='id desc')) == 0:
            lastId = 1
            return "HIST/"+str(lastId)
        else:
            lastId = self.env['clinica_veterinaria.historial_model'].search([], order='id desc')[0].id
            return "HIST/"+str(lastId+1)
        return True

    @api.onchange('cliente')
    def _getMascotas(self):
        for rec in self:
            return {'domain': {'mascota':[('cliente.id', '=', rec.cliente.id)]}}

    @api.one
    @api.constrains('fecha')
    def _checkDate(self):
        hoy = datetime.today()
        if (self.fecha < hoy):
            raise ValidationError("La fecha no puede ser anterior a hoy!")