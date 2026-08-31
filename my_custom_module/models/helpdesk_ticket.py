from odoo import models, fields, api
from datetime import timedelta

class HelpdeskTicket(models.Model):
    _inherit = 'helpdesk.ticket'

    @api.model
    def _cron_auto_close_tickets(self):
        # Fetch Resolved and Closed stages
        resolved_stage = self.env['helpdesk.stage'].search([('name', '=ilike', 'Resolved')], limit=1)
        closed_stage = self.env['helpdesk.stage'].search([('name', '=ilike', 'Closed')], limit=1)

        if not resolved_stage or not closed_stage:
            return

        # Calculate threshold date (7 days ago)
        date_threshold = fields.Datetime.now() - timedelta(days=7)

        # Search for tickets in 'Resolved' stage updated 7+ days ago
        tickets_to_close = self.search([
            ('stage_id', '=', resolved_stage.id),
            ('write_date', '<=', date_threshold)
        ])

        # Batch update stage to 'Closed'
        tickets_to_close.write({'stage_id': closed_stage.id})