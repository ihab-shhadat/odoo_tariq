# -*- coding: utf-8 -*-

from odoo import api, fields, models, _


class Partner(models.Model):
    _inherit = 'res.partner'
    national_number = fields.Char('National Number')
    passport_number = fields.Char('Passport Number')
    category_id = fields.Many2many('res.partner.category', column1='partner_id',
                                   column2='category_id', string='صفة الموكل')
    agent_for = fields.Char('وكيل عن')
    agency_no = fields.Char('Agency No')
    opponent_name = fields.Char("opponent name")
    lawyer_name = fields.Char("Lawyer's name")
    case_count = fields.Integer(compute='_compute_case_count', string='Case Count')
    case_ids = fields.One2many('lawfirm_case.case', 'partner_id', 'Case Ids')

    def _compute_case_count(self):
        all_partners = self.with_context(active_test=False).search([('id', '=', self.ids)])
        all_partners.read(['parent_id'])

        case_groups = self.env['lawfirm_case.case'].read_group(
            domain=[('partner_id', 'in', all_partners.ids)],
            fields=['partner_id'], groupby=['partner_id']
        )
        partners = self.browse()
        for group in case_groups:
            partner = self.browse(group['partner_id'][0])
            while partner:
                if partner in self:
                    partner.case_count += group['partner_id_count']
                    partners |= partner
                partner = partner.parent_id
        (self - partners).case_count = 0
