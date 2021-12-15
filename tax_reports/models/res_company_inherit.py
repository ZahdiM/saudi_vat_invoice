from odoo import api, fields, models

class ResCompanyClass(models.Model):
    _inherit = 'res.company'


    arabic = fields.Char('Arabic Name')
    building_no = fields.Char('Building No')
    district = fields.Many2one('district.details', string="District")
    group_vat_no = fields.Char('Group Vat No')
    comp_acc_detail = fields.Html('Company Account Detail')
    other_seller_id = fields.Char('Other Seller Id')
    additional_no = fields.Char('Additional No')

