# -*- coding: utf-8 -*-

from odoo import models, fields, api, tools

INV_TYPE_MAP = {
    'out_invoice': 'income',
    'out_refund': 'income',
    'in_invoice': 'expense',
    'in_refund': 'expense',
}

class AccountInvoiceLine(models.Model):
    _inherit = 'account.invoice.line'

    @api.onchange('product_id')
    def _onchange_product_id(self):
        res = super(AccountInvoiceLine, self)._onchange_product_id()
        inv_type = self.invoice_id.type
        if self.product_id:
            ana_accounts = self.product_id.product_tmpl_id.\
                _get_product_analytic_distributions()
            ana_account = ana_accounts[INV_TYPE_MAP[inv_type]]
            self.analytic_distribution_id = ana_account.id
        return res

class AccountReportInvoiceProduct(models.Model):
        _name = 'account.report.invoice.product'
        _description = 'account.report.invoice.product'
        _auto = False

        date_invoice = fields.Text(string='Mes factura')
        state_id = fields.Many2one('res.country.state',string='Estado')
        categ_id = fields.Many2one('product.category',string='Categoria')
        price_subtotal = fields.Float(string='Facturación Neta (sin IVA)')

        @api.model_cr
        def init(self):
                tools.drop_view_if_exists(self._cr,'account_report_invoice_product')
                self._cr.execute(""" create view account_report_invoice_product as (
                                    select max(ail.id) as id, 
                                    substring(cast(ai.date_invoice as text),1,7) as date_invoice, 
                                    ai.state_id, pt.categ_id, 
                                    sum(ail.price_subtotal) as price_subtotal
                                    from account_invoice ai
                                    left join account_invoice_line ail on ail.invoice_id = ai.id
                                    left join product_product pp on ail.product_id = pp.id
                                    left join product_template pt on pt.id = pp.product_tmpl_id
                                    /*left join product_category pc on pc.id = pt.categ_id*/
                                    /*left join res_country_state rce on rce.id = ai.state_id*/
                                    where ai."type" = 'out_invoice'
                                    and ai.state <> 'draft' 
                                    group by 2,3,4
                        ) """)
                        