from odoo import models, fields
from datetime import datetime


class SaleWizard(models.TransientModel):
    _name = "sale.wizard"

   
    
    order_date = fields.Datetime(string='Order DateTime', default=fields.Datetime.now)
    service_id = fields.Many2one("sale.order", string="Servicelog")
    
    bulk_order_line_ids = fields.One2many('bulk.order.line','sale_wizard_id',string="Sale Line")
    
    
    
    
    
    
    
    def action_create_sale_orders(self):
        SaleOrder = self.env['sale.order']
        SaleOrderLine = self.env['sale.order.line']

        for line in self.bulk_order_line_ids:
            # Create Sale Order for each partner if not exists
            sale_order = SaleOrder.create({
                'partner_id': line.partner_id.id,
                'pet_id': line.pet_id.id,
                'date_order': self.order_date,
                'origin': 'Wizard Order',
            })

            # Create Sale Order Line
            SaleOrderLine.create({
                'order_id': sale_order.id,
                'product_id': line.product_template_id.product_variant_id.id,
                'name': line.product_template_id.name,
                'product_uom_qty': line.quantity,
                'price_unit': line.unit_price,
                'tax_id': [(6, 0, line.tax_ids.ids)],
                'discount': line.disc,
            })

        return {
            'type': 'ir.actions.act_window',
            'name': 'Sale Orders',
            'res_model': 'sale.order',
            'view_mode': 'list,form',
            'target': 'current',
        }

    
    
    
    

		
    
    
    
    
		
		
	 
    
    
    
    
	
    
class BulkOrderLine(models.TransientModel):
		
	_name="bulk.order.line"
	
	sale_wizard_id = fields.Many2one('sale.wizard',string="Sale Id")
	partner_id = fields.Many2one('res.partner',string="Partner")
	pet_id = fields.Many2one('pet.pet',string="Pet")
	product_template_id = fields.Many2one('product.template',string="Product")
	quantity = fields.Float(string="Quantity")
	delivered = fields.Float(string="Delivered")
	invoiced = fields.Float(string="Invoiced")
	unit_price = fields.Float(string="Unit Price")
	tax_ids = fields.Many2many('account.tax',string="Taxes")
	disc = fields.Float(string="Disc")
	
	amount = fields.Monetary(string="Amount", currency_field='currency_id')
	currency_id = fields.Many2one('res.currency', string="Currency")
    

		
	
	    
    

    