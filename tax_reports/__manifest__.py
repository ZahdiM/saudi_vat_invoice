{
    # App information
    'name': 'KSA VAT Invoice/Simplified VAT Reports/Standard and B2C VAT Invoices فاتورة ضريبیة',
    'version': '14.0.1.3',
    'category': 'Sales',
    'summary': 'This Module will help in printing the Standard as well as B2C VAT Invoices',
    'description': """ Simplified Tax Report
    Simplified VAT Report
    Saudi Arabia VAT Invoice
    VAT E-Invoice Standard
    E-Invoicing
    B2C VAT Invoice
    Fatora 
    فاتورة ضريبیة
    """,
    'license': 'OPL-1',
    'depends':['sale_management','base','web','account'],

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
    "images": ['static/description/Banner.png'],
    'demo_xml': [],
    'installable': True,
    'auto_install': False,
    'application': True,
    'price': 30.00,
    'currency': 'USD',
}
