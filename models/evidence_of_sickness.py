from odoo import api, fields, models
from odoo.addons.project.models import project


class BeteglapNyilvantartas(models.Model):
    _name = "evidence.of.sickness"
    _description = "Evidence Of Sickness"
    

    company_id = fields.Many2one('res.partner', string='Company name')
    employee_id = fields.Many2one('res.partner', string='Employee')
    month = fields.Date(string='Month')
    file_number = fields.Char(string='File number')
    delivery_date = fields.Date(string='Delivery date')
    comment = fields.Char(string='Comment')
    status = fields.Selection([('ok','OK'),('deliver','Deliver'),('correct','Correct')], string='Status')
