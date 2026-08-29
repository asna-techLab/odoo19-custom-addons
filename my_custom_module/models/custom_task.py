from odoo import models,fields
class CustomTask(models.Model):
    _name = "custom_task"
    _description = "Custom Task Manager"

    name = fields.Char(string='Task Title', required=True)
    description = fields.Text(string='Description')
    is_completed = fields.Boolean(string='Completed', default=False)
    priority = fields.Selection([
        ('low', 'Low'),
        ('medium', 'Medium'),
        ('high', 'High'),
    ], string='Priority', default='medium')
