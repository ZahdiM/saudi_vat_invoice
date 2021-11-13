from odoo import api, fields, models
from datetime import timedelta

class InvoiceInherit(models.Model):
    _inherit = 'account.move'

    date_of_supply = fields.Date('Date of Supply')

    def _get_tax_report_base_filename(self):

        self.ensure_one()
        return "%s - %s - %s"%(self.company_id.vat,"{:%Y-%m-%d %H_%M_%S}".format(self.create_date.now()+timedelta(hours=3)),self.payment_reference)

    def _get_e_invoice_tax_report_base_filename(self):

        self.ensure_one()
        return "%s - %s - %s"%(self.company_id.vat,"{:%Y-%m-%d %H_%M_%S}".format(self.create_date.now()+timedelta(hours=3)),self.payment_reference)

    # def get_inv(self,order_id):
    #     invoices = order_id.order_line.invoice_lines.move_id.filtered(lambda r: r.move_type in ('out_invoice', 'out_refund'))
    #     invoice_id = self.env['account.move'].search([('id','in',invoices.ids)],order='create_date desc', limit=1)
    #     return invoice_id


class InvoiceLineInherit(models.Model):
    _inherit='account.move.line'


    def get_tax(self,inv_line):
        first_tax_id= False
        for tax_id in inv_line.tax_ids:
            if tax_id:
                first_tax_id = tax_id
                break
        return first_tax_id



