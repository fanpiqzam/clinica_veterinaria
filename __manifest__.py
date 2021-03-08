# -*- coding: utf-8 -*-
{
    'name': "clinica_veterinaria",

    'summary': "Gestión de una clínica veterinaria",

    'description': "Mediante este módulo se podrá gestionar una clínica veterinaria.",

    'author': "Fanny",
    'website': "http://www.yourcompany.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/12.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base',
        'mail'],

    # always loaded
    'data': [
        'security/clinica_veterinaria_security.xml',
        'security/ir.model.access.csv',
        'views/clinica_view.xml',
        'views/veterinario_view.xml',
        'views/mascota_view.xml',
        'views/historial_view.xml',
        'views/cliente_view.xml',
        'views/servicios_view.xml',
        'views/factura_view.xml',
        'views/detallefac_view.xml',
        'views/menu_view.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
    'application':True,
    'installable':True,
}
