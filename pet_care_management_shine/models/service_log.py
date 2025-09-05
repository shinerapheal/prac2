from odoo import fields, api, models
from datetime import datetime
from odoo.exceptions import ValidationError

class ServiceLog(models.Model):
	
	_name = "service.log"
	_description = "model for service log"
	
	customer = fields.Many2one('res.partner',string="Customer",domain=[('petowner','=','True')])
	pet = fields.Many2one('pet.pet',string='Pet')
	current_datetime = fields.Datetime(string='Current DateTime', default=fields.Datetime.now)
	service = fields.Many2one('product.template',string="Servives",domain=[('is_pet_service','=','True')])
	total_time_assigned = fields.Float(string='Assigned Time', help="Time in hours (e.g., 2.5 for 2 hours 30 minutes)")
	
	service_log_ids = fields.One2many('service.log.line','service_log_id',string="Lines")
	feedback = fields.Char(string="Feedback")
	total_hours_spend = fields.Float(string='Total Hours Spend', compute="compute_total",default=0)
	
	@api.depends('service_log_ids')
	def compute_total(self):
		for rec in self:
			if rec:
				for time in rec.service_log_ids:
					rec.total_hours_spend += time.time_spend
					
	@api.onchange('customer')
	def _onchange_customer(self):
	    if self.customer:
	        pets = self.env['pet.pet'].search([('owner_id', '=', self.customer.id)])
	        pet_ids = []
	        for i in pets:
	        	print(i.id)
	        	pet_ids.append(i.id)
	        print(pet_ids)
	        return {
	            'domain': {
	                'pet': [('id', '=', pet_ids)]
	            }
	        }
	    else:
	        return {
	            'domain': {
	                'pet': [('id', 'in', [])]
	            }
	        }
					
					
	def unlink(self):
		for record in self:
			
			if record.service_log_ids != 0:
				raise ValidationError("Cannot delete registered log")
		return super(service.log, self).unlink()

		
					
	
       			
					
			
				
	
class ServiceLogLine(models.Model):
        _name = "service.log.line"
        _discription = "Service Log Line"
        
        
        service_log_id = fields.Many2one('service.log',string='Service Log')
        employee_id = fields.Many2one('hr.employee',string="Employee")
        work_done = fields.Char(string="Work Done")
        status = fields.Selection([('started','started'),('inprogress','inprogress'),('partial','partial'),('completed','completed')])
        time_spend = fields.Float(string="Time Spend")
            
        
        
        