# -*- coding: utf-8 -*-

import re
from datetime import datetime
from datetime import date
from dateutil.relativedelta import relativedelta
from odoo import models, fields, api, tools, exceptions, _
from odoo.tools import DEFAULT_SERVER_DATETIME_FORMAT
from odoo.exceptions import ValidationError
from odoo.osv import expression
from odoo.tools import float_compare, pycompat
from odoo.addons import decimal_precision as dp

class PaiementInfos(models.Model):
    _name = 'gc.paiement.info'
    _rec_name = 'name'

    name = fields.Many2one('res.partner', string="Member", domain=[('customer', '=', True),('member_type','=','member')])
    member_reference = fields.Char(related='name.reference_internal', string="Member Reference", readonly=True)

    is_this_month_paid = fields.Selection([('yes', 'Yes'),('no', 'No')], string="Is this month paid ?")
    saving_paiements = fields.One2many('gc.paiements', 'paiement_id', string="Paiements")


class Paiements(models.Model):
    _name = 'gc.paiements'

    paiement_id = fields.Many2one('gc.paiement.info', ondelete='cascade', string="Paiements")
    paiement_type = fields.Selection([('fees', 'Subscription Fees'),('insurance', 'Insurance'),('other_paiement','Other Paiement')])
    start_date = fields.Date(string="Paiement Period : Start")
    end_date = fields.Date(string="Paiement Period : End")
    activity_id = fields.Many2one('gc.activity', string="Activity")
    amount_id = fields.Float(string="Amount Paid")
    paiement_notes = fields.Text(string="Notes")
