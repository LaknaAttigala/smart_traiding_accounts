# -*- coding: utf-8 -*-

from flectra import models, fields, api



class Partner(models.Model):
    _inherit = 'res.partner'


    cus_tax_types= fields.Selection([('tax','Tax Invoice'),('stax','Suspended Tax'),('alltax','All Inclusive'),('comtax','Commercial'),('protax','Proforma')]
    , string='Tax Types', default='tax')



class AccountInvoice(models.Model):
    _inherit = "account.invoice"

    cus_tax_types= fields.Selection([('tax','Tax Invoice'),('stax','Suspended Tax'),('alltax','All Inclusive'),('comtax','Commercial'),('protax','Proforma')], string='Tax Types')
    suspended_tax = fields.Monetary(string="Suspended V.A.T. 8%", compute='_compute_svat_total')
    
    @api.depends('amount_total', 'cus_tax_types')
    def _compute_svat_total(self):
        for tax_line in self:
            if tax_line.amount_total:
                tax_line.suspended_tax = (tax_line.amount_total*8)/100

    @api.onchange('partner_id')
    def get_customer_tax_type(self):
        if self.partner_id:
            self.cus_tax_types= self.partner_id.cus_tax_types
    
    @api.multi
    def new_invoice_print(self):       
        self.ensure_one()
        if self.cus_tax_types=='stax':        
            return self.env.ref('smart_traiding_accounts.smart_invoice_lkr_stax_menu').report_action(self)
        if self.cus_tax_types=='alltax':        
            return self.env.ref('smart_traiding_accounts.smart_invoice_alltax_menu').report_action(self)
        if self.cus_tax_types=='comtax':
            return self.env.ref('smart_trading_reports_lakna.smart_invoice_commercial_menu').report_action(self)
        if self.cus_tax_types=='protax':
            return self.env.ref('smart_trading_reports_lakna.smart_invoice_export_pro_forma_menu').report_action(self)
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