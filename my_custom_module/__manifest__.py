{
    'name': 'Custom Task Manager',
    'version': '1.0',
    'summary': 'Manage custom tasks in Odoo 19',
    'category': 'Services',
    'author': 'Your Name',
    'license': 'LGPL-3',
    'depends': ['base','mail','helpdesk','account','crm'],
    'data': [
        'security/ir.model.access.csv',
        'views/custom_task_views.xml',
        'data/cron_data.xml',
        'data/mail_template_data/xml'
        'data/crm_data.xml',
    ],
    'installable': True,
    'application': True,
}