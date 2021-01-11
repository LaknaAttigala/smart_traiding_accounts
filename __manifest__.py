# -*- coding: utf-8 -*-
{
    'name': "smart traiding accounts",

    'summary': """
        Short """,

    'description': """
        Long description of module's purpose
    """,

    'author': "DM Prabath",
    'website': "http://www.codeso.lk",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/flectra/flectra/blob/master/flectra/addons/base/module/module_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base','account'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        'views/new_report_template.xml',
        'views/views.xml',
        'views/templates.xml',

        'reports/invoice_lkr_tax_report.xml',
        'reports/menu_report.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}