# -*- coding: utf-8 -*-

from odoo import models, fields, api

class ProductTemplate(models.Model):
    _inherit = ['product.template']

    income_analytic_distribution_id = fields.Many2one(
        comodel_name='account.analytic.distribution',
        string='Income Analytic distribution',
        company_dependent=True
    )

    expense_analytic_distribution_id = fields.Many2one(
        comodel_name='account.analytic.distribution',
        string='Expense Analytic distribution',        
        company_dependent=True
    )

    @api.multi
    def _get_product_analytic_distributions(self):
        self.ensure_one()
        return {
            'income': self.income_analytic_distribution_id,
            'expense': self.expense_analytic_distribution_id
        }