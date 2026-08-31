from odoo import models, fields, api
from datetime import timedelta

class HelpdeskTicket(models.Model):
    _inherit = 'helpdesk.ticket'

    @api.model
    def _cron_auto_close_tickets(self):
        resolved_stage = self.env['helpdesk.stage'].sudo().search(
            [('name', '=ilike', 'Resolved')],
            limit=1
        )

        closed_stage = self.env['helpdesk.stage'].sudo().search(
            [('name', '=ilike', 'Closed')],
            limit=1
        )

        if not resolved_stage or not closed_stage:
            return

        date_threshold = fields.Datetime.now() - timedelta(days=7)

        tickets_to_close = self.sudo().search([
            ('stage_id', '=', resolved_stage.id),
            ('write_date', '<=', date_threshold)
        ])

        tickets_to_close.write({
            'stage_id': closed_stage.id
        })