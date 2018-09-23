# -*- coding: utf-8 -*-
{
    'name': "GymCRM",

    'summary': """""",

    'description': """
    """,

    'author': "GoAddons",
    'website': "http://www.goaddons.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/master/odoo/addons/base/module/module_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        'views/member.xml',
        'views/activity.xml',
        'views/paiement.xml',

    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}