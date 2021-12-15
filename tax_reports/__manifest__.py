{
    # App information
    'name': 'Tax Report',
    'version': '14.0.1.3',
    'category': 'Sales',
    'summary': 'This Module will help in printing the Reports for Sales Order',
    'license': 'OPL-1',
    'depends':['base','account'],

    # Author
    'author': 'Mediod Consulting Pvt. Ltd.',
    'website': 'http://www.mediodconsulting.com/',
    'maintainer': 'Mediod Consulting Pvt. Ltd.',

    # Views
    'init_xml': [],
    'data': [
        'security/ir.model.access.csv',
        'security/security.xml',
        'view/sale_order_inherit_view.xml',
        'view/res_partner_inherit_view.xml',
        'view/res_company_inherit_view.xml',
        'reports/report.xml',
        'reports/sale_order_report.xml',
        'reports/e_invoicing_b2c.xml',
        # 'view/inherit_web_external_layout.xml'
    ],
    "images":['static/description/Banner.png','static/description/Thumbnail.png','static/description/icon.png'],
    'demo_xml': [],
    'installable': True,
    'auto_install': False,
    'application': True,
    'price': 379.00,
    'currency': 'EUR',
}
