from odoo import models, fields, api
from datetime import datetime 
from odoo.exceptions import ValidationError
class PetOwner(models.Model):
	_inherit = 'res.partner'
	
	
	
	
	
	pet_ids = fields.One2many('pet.pet','owner_id' ,readonly=True)
	petowner = fields.Boolean(string="Is Pet Owner", default=True)
	loyalty_points = fields.Integer(string='Loyalty Points', default=0)

	@api.constrains('mobile')
	def check_mobile(self):
		for rec in self:
			if len(rec.mobile) != 10:
				raise ValidationError('mobile number should be a 10 digit one') 
			
	@api.constrains('phone')
	def check_phone(self):
		for rec in self:
			if len(rec.phone) != 10:
				raise ValidationError('phone number should be a 10 digit one') 		
			
	@api.constrains('email')
	def _check_email(self):
		for rec in self:
			 if "@" not in rec.email or "." not in rec.email:
	                    raise ValidationError("The email address must contain '@' and '.'")	
	                    
	                    
	def update_service(self):
		records_to_email = self.search([('petowner', '=', 'True')])
		
		template = self.env.ref('pet_care_management_shine.service_reminder')
	
		for rec in records_to_email:
			
			
			template.send_mail(rec.id)	                    
	                    
	                    