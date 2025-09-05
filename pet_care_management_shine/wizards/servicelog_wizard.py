from odoo import models, fields


class ServicelogWizard(models.TransientModel):
	_name = "servicelog.wizard"
	
	
	message_string = fields.Text(string="Message")
	number = fields.Char(string="Phone")
	
	
	def send_feedback(self):
		active = self.env.context.get(active_id)
		print(active.id)
		message_string=self.message_string
		number = self.number
		link = f"https://web.whatsapp.com/send?phone={number}&text={message_string}"
		send_msg = {
	        'type': 'ir.actions.act_url',
	        'url': link,
	        'target': 'new',
	        'res_id': self.id}
		return send_msg

    
    			