from odoo import models, api, fields


class PetInvoice(models.Model):
	_inherit = 'account.move'
	