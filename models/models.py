# -*- coding: utf-8 -*-

from flectra import models, fields, api



class Partner(models.Model):
    _inherit = 'res.partner'


    cus_tax_types= fields.Selection([('tax','Tax Invoice'),('stax','Suspended Tax'),('alltax','All Inclusive'),('comtax','Commercial')]
    , string='Tax Types', default='tax')



class AccountInvoice(models.Model):
    _inherit = "account.invoice"

    cus_tax_types= fields.Selection([('tax','Tax Invoice'),('stax','Suspended Tax'),('alltax','All Inclusive'),('comtax','Commercial')]
    , string='Tax Types')


    @api.onchange('partner_id')
    def get_customer_tax_type(self):
        if self.partner_id:
            self.cus_tax_types= self.partner_id.cus_tax_types
    
    @api.multi
    def new_invoice_print(self):       
        self.ensure_one()
        if self.currency_id.name!="LKR":        
            return self.env.ref('smart_traiding_accounts.smart_invoice_lkr_tax_menu').report_action(self)
        else:        
            return self.env.ref('smart_traiding_accounts.smart_invoice_lkr_tax_menu').report_action(self)
# class smart_traiding_accounts(models.Model):
#     _name = 'smart_traiding_accounts.smart_traiding_accounts'

#     name = fields.Char()
#     value = fields.Integer()
#     value2 = fields.Float(compute="_value_pc", store=True)
#     description = fields.Text()
#
#     @api.depends('value')
#     def _value_pc(self):
#         self.value2 = float(self.value) / 100