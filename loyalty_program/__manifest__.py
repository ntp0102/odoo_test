# -*- coding: utf-8 -*-
{
    'name': "loyalty_program",

    'summary': """
        Short (1 phrase/line) summary of the module's purpose, used as
        subtitle on modules listing or apps.openerp.com""",

    'description': """
        Long description of module's purpose
    """,

    'author': "My Company",
    'website': "http://www.yourcompany.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/14.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base','product','sale'],

    # always loaded
    'data': [
        'security/ir.model.access.csv',
        'views/views.xml',
        'views/templates.xml',
        'views/program_views.xml',
        'views/customer_views.xml',
        'views/history_views.xml',
        'views/partner_levels_views.xml',
        'views/res_config_setting_views.xml',
        'report/report_history.xml',
        'report/report_history_template.xml',
        'views/report_dashboard.xml',
        # 'data/program.csv',
        # 'data/partner.levels.csv'
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
    'installable': True,
    'application': True,
}
