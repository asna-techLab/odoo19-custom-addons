from odoo import models, api, fields
import datetime

class CrmLead(models.Model):
    _inherit = 'crm.lead'

    @api.model
    def _cron_send_daily_lead_summary(self):
        today_start = datetime.datetime.now().replace(hour=0, minute=0, second=0, microsecond=0)
        new_leads = self.search([('create_date', '>=', today_start)])

        if new_leads:
            lead_rows = "".join([
                f"<li><strong>{lead.name}</strong> - Contact: {lead.partner_id.name or lead.contact_name or 'N/A'}</li>"
                for lead in new_leads
            ])

            body_html = f"""
            <p>Hello Sales Manager,</p>
            <p>A total of <strong>{len(new_leads)}</strong> new lead(s) were created today:</p>
            <ul>{lead_rows}</ul>
            """

            self.env['mail.mail'].create({
                'subject': f"Daily Lead Summary ({fields.Date.today()})",
                'body_html': body_html,
                'email_to': 'sales_manager@example.com',
            }).send()