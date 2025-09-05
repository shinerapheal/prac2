from odoo import models,fields,api
from odoo.exceptions import ValidationError
class serviceBooking(models.Model):
	_inherit = 'sale.order'
	
	
	pet_id = fields.Many2one('pet.pet',string="Pet")
	earned_loyalty_points = fields.Integer(string='Earned Loyalty Points', compute='_compute_loyalty_points', store=True)
	feedback = fields.Char(string='FeedBack')
	
	
	
	
	
	@api.constrains('state')
	def slot_decrement(self):
		for rec in self:
			if rec.state == 'draft':
				rec.order_line.product_template_id.available_slotes -= 1
			elif rec.state == 'cancel':
				rec.order_line.product_template_id.available_slotes += 1	
			elif rec.state == 'draft' and rec.order_line.product_template_id.available_slotes == 0:
				raise ValidationError('No slots Available Today Try Tommorow')
	
					
	@api.onchange('customer')
	def _onchange_customer(self):
	    if self.customer:
	        return {
	            'domain': {
	                'pet': [('owner_id', '=', self.customer.id)]
	            }
	        }
	    else:
	        return {
	            'domain': {
	                'pet': []
	            }
	        }	
				
	@api.depends('amount_total')				
	def _compute_loyalty_points(self):
		for order in self:
			order.earned_loyalty_points = int(order.amount_total // 10)		
			print(order.amount_total // 10)	
			
	def action_confirm(self):
		res = super(serviceBooking, self).action_confirm()
		for order in self:
			if order.partner_id:
				order.partner_id.loyalty_points += order.earned_loyalty_points
		return res	
				
	
			
				