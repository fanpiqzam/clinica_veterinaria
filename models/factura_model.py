# -*- coding: utf-8 -*-

from odoo import models, fields, api
from odoo.exceptions import ValidationError
import datetime
import logging
_logger = logging.getLogger(__name__)

class factura_model(models.Model):
    _name = 'clinica_veterinaria.factura_model'
    _sql_constraints = [
        ('ref_unica','UNIQUE(name)','No puede haber dos facturas con la misma referencia!'),
    ]

    name = fields.Char('Ref', required=True, index=True, default=lambda self:self._generaRef())
    fecha = fields.Date('Fecha', default=datetime.date.today())
    cliente = fields.Many2one('clinica_veterinaria.cliente_model')
    detalle = fields.One2many('clinica_veterinaria.detallefac_model','factura', ondelete='cascade')
    base = fields.Float('Base', compute="_calculateBase", store=True)
    iva = fields.Selection([("21","21%"),("15","15%"),("7","7%"),("0","0%")], string="IVA",default="21")
    total = fields.Float('Total', compute="_calculateTotal", store=True)
    is_done = fields.Boolean('¿Pagada?', default=False)

    @api.model
    def _generaRef(self):
        #lastId = self.env['clinica_veterinaria.factura_model'].search([], order='id desc')[0].id
        if len(self.env['clinica_veterinaria.factura_model'].search([], order='id desc')) == 0:
            lastId = 1
            return "INV/"+str(datetime.date.today().year)+"/"+str(lastId)
        else:
            lastId = self.env['clinica_veterinaria.factura_model'].search([], order='id desc')[0].id
            return "INV/"+str(datetime.date.today().year)+"/"+str(lastId+1)
        return True

    @api.one
    @api.depends('detalle','iva')
    def _calculateBase(self):
        total = 0
        for det in self.detalle:
            cantidad = det.cantidad
            precio = det.servicio.precio
            total += cantidad*precio
        self.base = total
        return True
    
    @api.one
    @api.depends('detalle','iva')
    def _calculateTotal(self):
        iva = ((self.base*float(self.iva))/100)
        self.total = self.base+iva
        return True