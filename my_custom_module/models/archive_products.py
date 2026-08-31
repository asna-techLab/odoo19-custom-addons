from odoo import models, fields, api


class ProductTemplate(models.Model):
    _inherit = 'product.template'

    # Custom expiration date field
    expiration_date = fields.Date(string='Expiration Date')

    @api.model
    def archive_expired_products(self):
        today = fields.Date.today()

        # Search for active products where expiration date is in the past
        expired_products = self.search([
            ('expiration_date', '<', today),
            ('active', '=', True)
        ])

        if expired_products:
            # Use Odoo's built-in archive method
            expired_products.action_archive()

            # Post chatter log on archived records
            for product in expired_products:
                product.message_post(
                    body="<p><strong>System Alert:</strong> Product automatically archived due to reaching expiration date.</p>"
                )