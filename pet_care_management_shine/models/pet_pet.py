from odoo import models,fields,api,_
from datetime import datetime
from odoo.exceptions import ValidationError

class PetPet(models.Model):
	_name = "pet.pet"
	_description = "pet_details"
	_inherit = ['mail.thread']
	
	name = fields.Char(string="Name",required=True)
	species = fields.Selection(selection=[('dog', 'dog'),('cat','cat')])
	gender = fields.Selection(selection=[('female', 'Female'),('male','Male')])
	breed = fields.Char(string="Breed" , required=True)
	date_of_birth = fields.Date(string="Date of Birth",required=True)
	age = fields.Integer(string="age" , compute="compute_age")
	owner_id = fields.Many2one('res.partner',string="Owner")
	sequence_number = fields.Char(string="Sequence Number", default=lambda self: _('/'), readonly=True, 
                                  copy=False, help="Sequence Number ")
	sale_ids = fields.One2many('sale.order','pet_id' ,readonly=True,tracking=True)
	pet_description = fields.Text(string="Pet Description")
	pet_weight = fields.Float(string="Pet Weight",tracking=True)
	active = fields.Boolean(string="Active",default=True)
	
	service_ids = fields.Many2many('product.template', string="Pet Services",
                                   domain=[('is_pet_service', '=', True)],
                                   help="Services availed by the pet.",tracking=True)
	
	@api.model
	def create(self, vals):
		if vals.get('sequence_number', _('/')) == _('/'):
			vals['sequence_number'] = self.env['ir.sequence'].next_by_code('pet.sequence')
		return super(PetPet, self).create(vals)
	
	
	
	@api.onchange('species')
	def species_onchange(self):
		if self.species == 'dog':
			self.breed = 'labourbor'
		elif self.species == 'cat':
			self.breed = 'persian'	
			
			
	
	def compute_age(self):
		self.age = datetime.today().year - self.date_of_birth.year
	   		
	def smart_appoitment(self):
         return {
            'type': 'ir.actions.act_window',
            'name': 'Appointment',
            'view_mode': 'list',
            'res_model': 'sale.order',
            'domain': [('id', 'in', self.sale_ids.ids)],
            'context': {'create': False},
        }        
 	   		
	@api.model
	def action_decativateall(self):
		for rec in self:
			if rec:
				records_to_update = rec.search([('active', '=', True)])
				records_to_update.write({'active': False})
				
				
	@api.model
	def action_decativateselected(self):
		for rec in self:
			if rec:
				rec.active=False

				
				
				
			
	def unlink(self):
		for record in self:
			
			if record.active == True:
				raise ValidationError("Cannot delete Active Pet")
		return super(pet.pet, self).unlink()

		
	   		
	   		
				
		
	
	

