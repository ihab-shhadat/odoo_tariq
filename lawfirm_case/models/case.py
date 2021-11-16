# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

from odoo import fields, models
from odoo.addons.base.models.res_partner import WARNING_MESSAGE, WARNING_HELP


class Case(models.Model):
    _name = 'lawfirm_case.case'

    partner_id = fields.Many2one(
        'res.partner', string='Customer',
        readonly=True,
        required=True, change_default=True, index=True, tracking=1,
    )
    case_seq = fields.Char('الرقم المتسلسل')
    case_office = fields.Char('الرقم القضية المكتبي')
    case_num = fields.Char('درجة القضية الاساسي')
    degree_litigation = fields.Selection([
        ('degree_one', 'درجة اولى'),
        ('resumption', 'استئناف'),
        ('change', 'تغير')], string='درجة التقاضي', default='degree_one', required=True,
    )
    case_type = fields.Selection([
        ('rights', 'حقوق'),
        ('penalty', 'جزاء'),
    ], string='درجة التقاضي', default='rights', required=True,
    )
    court_name = fields.Char('اسم المحكمة')
    case_subject = fields.Char('موضوع القضية')
    case_type = fields.Selection([
        ('rights', 'منظوره'),
        ('separated', 'مفصولة'),
    ], string='حالة الدعوى', default='rights', required=True,
    )
