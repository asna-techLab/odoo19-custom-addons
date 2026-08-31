from odoo import models, fields, api


class ProductTemplate(models.Model):
    _inherit = 'product.template'

    expiration_date = fields.Date(string='Expiration Date')

    @api.model
    def archive_expired_products(self):
        today = fields.Date.today()

        # Run search with sudo permissions
        expired_products = self.sudo().search([
            ('expiration_date', '<', today),
            ('active', '=', True)
        ])

        if expired_products:
            expired_products.action_archive()
            for product in expired_products:
                product.message_post(
                    body="<p><strong>System Alert:</strong> Product automatically archived due to reaching expiration date.</p>"
                )