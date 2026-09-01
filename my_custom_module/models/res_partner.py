from odoo import models, api


class ResPartner(models.Model):
    _inherit = 'res.partner'

    @api.model_create_multi
    def create(self, vals_list):
        # Create the partner records using Odoo's base logic
        records = super().create(vals_list)

        # Post the welcome message to the Chatter for each newly created partner
        for record in records:
            record.message_post(
                body="Welcome!..... A new contact profile has been successfully created.",
                message_type="comment",
                subtype_xmlid="mail.mt_note"
            )
        return records