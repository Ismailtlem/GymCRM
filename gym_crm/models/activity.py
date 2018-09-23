# -*- coding: utf-8 -*-

from datetime import datetime
from datetime import date
from dateutil.relativedelta import relativedelta
from odoo import models, fields, api, tools, exceptions, _
from odoo.tools import DEFAULT_SERVER_DATETIME_FORMAT
import re
from odoo.exceptions import ValidationError
from odoo.osv import expression
from odoo.tools import float_compare, pycompat
from odoo.addons import decimal_precision as dp


class Activity(models.Model):
    _name = 'gc.activity'
    _rec_name = 'name'

    name = fields.Char(string="Name")
    prix = fields.Float(string="Subscription Fee", default=0.0)
	
    activity_id_member = fields.Many2one('res.partner', string="Paiements")
    activity_name = fields.Many2one('gc.activity', string="Activity")
    start_date_activity = fields.Date(string="Start Date")
    end_date_activity = fields.Date(string="End Date")
    paid_statut = fields.Selection([('yes', 'Yes'),('no', 'No')], string="Paid ?")
    activity_statut = fields.Selection([('yes', 'Yes'),('no', 'No')], compute='update_statut', string="Active ?", store=True)
    notes = fields.Text(string="Notes")
	
            # Paiement Status
    @api.model
    @api.depends('start_date_activity','end_date_activity')
    def update_statut(self):
        for r in self:
            if r.start_date_activity and r.end_date_activity:
                if r.start_date_activity <= fields.Date.to_string(date.today()) and r.end_date_activity >= fields.Date.to_string(date.today()):
                    r.activity_statut = 'yes'
                else:
                    r.activity_statut = 'no'
