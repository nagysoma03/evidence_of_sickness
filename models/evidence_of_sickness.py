from odoo import api, fields, models
from odoo.addons.project.models import project


class BeteglapNyilvantartas(models.Model):
    _name = "evidence.of.sickness"
    _description = "Evidence Of Sickness"
    _inherit = 'project.task'

    companyName = fields.Many2one('res.partner', string='Cég neve')
    employee = fields.Many2one('res.partner', string='Alkalmazott neve')
    month = fields.Date(string='Hónap')
    fileNumber = fields.Char(string='Iktatószám')
    deliveryDate = fields.Date('Leadás dátuma')
    comment = fields.Char('Megjegyzés')
    status = fields.Selection([('option1','OK'),('option2','Leadni'),('option3','Javítani')], string='Állapot')


    user_ids = fields.Many2many('res.users', relation='beteglap_task_user_ids_rel', column1='task_id', column2='user_id',
        string='Assignees', default=lambda self: not self.env.user.share and self.env.user, context={'active_test': False}, tracking=True)
    personal_stage_type_ids = fields.Many2many('project.task.type', 'beteglap_personal_stage_type_ids_rel', column1='task_id', column2='stage_id',
        ondelete='restrict', group_expand='_read_group_personal_stage_type_ids', copy=False,
        domain="[('user_id', '=', user.id)]", depends=['user_ids'], string='Personal Stage')
    depend_on_ids = fields.Many2many('project.task', relation="beteglap_depend_on_ids_rel", column1="task_id",
                                     column2="depends_on_id", string="Blocked By", tracking=True, copy=False,
                                     domain="[('allow_task_dependencies', '=', True), ('sid', '!=', id)]")
    dependent_ids = fields.Many2many('project.task', relation="beteglap_depend_on_ids_rel", column1="depends_on_id",
                                     column2="task_id", string="Block", copy=False,
                                     domain="[('allow_task_dependencies', '=', True), ('id', '!=', id)]")