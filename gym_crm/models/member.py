from datetime import datetime
from datetime import date
from odoo import api, fields, models, tools, _
from odoo.tools import float_compare, pycompat
from odoo.exceptions import ValidationError
from odoo.osv import expression

from odoo.addons import decimal_precision as dp

class Member(models.Model):
    _inherit = 'res.partner'

    member_type = fields.Selection([('member', 'Member'),('prospect', 'Prospect')])
    reference_internal = fields.Char(string="Internal Reference")
    subscription_date = fields.Date(string="Subscription Date")

    activity_member = fields.One2many('gc.activity', 'activity_id_member', string="Activities")

#Additional Infos

    function = fields.Char(string="Occupation")
    joining_date = fields.Date(string="Joining Date")

#Medical Infos

    emergency_contact = fields.Char(string="Emergency Contact")
    relationship = fields.Char(string="Relationship")
    email_contact = fields.Char(string="E-mail")
    contact_phone_number = fields.Char(string="Phone")
    medical_informations = fields.Text(string="Medical Notes")


    _sql_constraints = [     
    ('reference_internal_unique',
    'UNIQUE(reference_internal)',
    "This reference already exist"),
    ]
