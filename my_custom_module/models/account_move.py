from odoo import models, fields, api


class AccountMove(models.Model):
    _inherit = 'account.move'

    def write(self, vals):
        # Execute the standard update first
        res = super().write(vals)

        # Apply your exact requested filter domain to the records currently being updated
        domain = [
            ('id', 'in', self.ids),
            ('move_type', '=', 'out_invoice'),
            ('invoice_date_due', '<', fields.Date.today()),
            ('payment_state', 'not in', ('paid', 'in_payment', 'reversed'))  # Excludes already paid invoices
        ]

        overdue_invoices = self.search(domain)

        for move in overdue_invoices:
            template = self.env.ref('my_custom_module.email_template_overdue_invoice', raise_if_not_found=False)
            if template:
                # Send the email template
                template.send_mail(move.id, force_send=True)

        return res