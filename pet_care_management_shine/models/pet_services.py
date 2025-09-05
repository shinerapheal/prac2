from odoo import models,fields,api


class PetService(models.Model):
	_inherit = "product.template"
	
	description= fields.Text(string="Description")
	available_slotes = fields.Integer(string="Slots" ,default=10, readonly=True )
	is_pet_service = fields.Boolean(string="Is Pet Service", default=True)
	
	
	@api.model
	def update_slot(self):
		records_to_update = self.search([('is_pet_service', '=', 'True')])
		records_to_update.write({'available_slotes': '10'})
        
	



