from odoo import api, fields, models

class ResPartnerClass(models.Model):
    _inherit = 'res.partner'

    arabic_name = fields.Text('Arabic Name')
    building_no = fields.Char('Building No')
    district = fields.Many2one('district.details', string="District")
    group_vat_no = fields.Char('Group Vat No')
    other_buyer_id = fields.Char('Other Buyer Id')
    additional_no = fields.Char('Additional No')


class DistrictDetails(models.Model):
    _name = 'district.details'

    name = fields.Char('Name')

