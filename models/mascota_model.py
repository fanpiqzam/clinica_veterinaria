# -*- coding: utf-8 -*-

from odoo import models, fields, api

class mascota_model(models.Model):
    _name = "clinica_veterinaria.mascota_model"
    _sql_constraints = [
        ('numChip_unique','UNIQUE(numChip)','No puede haber dos número de ID iguales!'),
    ]
    
    numChip = fields.Char('Número identificador', required=True, default=lambda self:self._generaId())
    name = fields.Char('Nombre', required=True)
    peso = fields.Float('Peso', required=True)
    especie = fields.Char('Especie')
    visitas = fields.Integer('Visitas', compute="_contarVisitas")
    atienden = fields.One2many('clinica_veterinaria.atienden_model','mascota')
    historial = fields.One2many('clinica_veterinaria.historial_model','mascota')
    cliente = fields.Many2one('clinica_veterinaria.cliente_model')
    visitas = fields.Integer('Visitas', compute="_contarVisitas")

    
    @api.model
    def _generaId(self):
        #lastId = self.env['clinica_veterinaria.factura_model'].search([], order='id desc')[0].id
        if len(self.env['clinica_veterinaria.mascota_model'].search([], order='id desc')) == 0:
            lastId = 1
            return "MASC/"+str(lastId)
        else:
            lastId = self.env['clinica_veterinaria.mascota_model'].search([], order='id desc')[0].id
            return "MASC/"+str(lastId+1)
        return True

    @api.multi
    def borrarHistorial(self):
        self.visitas = 0
        for hist in self.historial:
            hist.unlink()
        return True

    @api.one
    def _contarVisitas(self):
        self.visitas = len(self.historial)
        return True