from odoo import models,api,fields


class HrEmployee(models.Model):
	
	_inherit = 'hr.employee'
	
	service_log_line_ids = fields.One2Many('service.log.line','employee_ids','Service Log')