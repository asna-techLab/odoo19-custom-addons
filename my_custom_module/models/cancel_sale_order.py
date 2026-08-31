from odoo import models, fields, api
from datetime import timedelta


class SaleOrder(models.Model):
    _inherit = 'sale.order'

    @api.model
    def _cron_auto_cancel_draft_orders(self):
        # Calculate threshold date (10 days ago from now)
        threshold_date = fields.Datetime.now() - timedelta(days=10)

        # Search for draft quotations created 10+ days ago
        draft_orders = self.search([
            ('state', '=', 'draft'),
            ('create_date', '<=', threshold_date)
        ])

        if draft_orders:
            # Call Odoo's native cancel method
            draft_orders.action_cancel()

            # Post chatter log on each canceled order
            for order in draft_orders:
                order.message_post(
                    body="<p><strong>System Alert:</strong> Quotation automatically canceled because it remained in Draft state for over 10 days.</p>"
                )