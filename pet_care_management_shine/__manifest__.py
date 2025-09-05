{
    'name': 'Pet Care Management Shine',
    'version': '18.0.0.0',
    'summary': 'This module is used for pet care mangement',
    'description': """This module is used for pet care mangement""",
    'category': 'project',
    'author': 'Shine Rapheal.',
    'website': 'www.zbeanztech.com',
    'depends': ['contacts','sale','account','report_xlsx','hr'],
    'data': [
               
        'security/ir.model.access.csv',
        'security/security.xml',
        'data/slot_sheduler_data.xml',
        'data/pet_sequence.xml',
        'data/service_reminder_email.xml',
        'data/email_scheduler.xml',
        
        'reports/pet_services_template.xml',
        'reports/report.xml',
        'reports/pet_report_xlsx.xml',
       
       'wizards/service_wizard_view.xml',
       'wizards/service_wizard_view.xml',
       'wizards/sale_wizard_view.xml',
       
      
       
       'views/pet_owner_views.xml',
       'views/pet_views.xml',
       'views/pet_services_views.xml',
       'views/service_booking_views.xml',
       'views/pet_quatation_view.xml',
       'views/pet_invoice_views.xml',
       'views/service_log_view.xml',
     
        
        'views/menu.xml',
        
        
        ],
    'assets': {
       
    },
    'test': [],
    'demo': [],
    'installable': True,
    'auto_install': False,
    'application': False,
}
