{
    'name': 'Custom Task Manager',
    'version': '1.0',
    'summary': 'Manage custom tasks in Odoo 19',
    'category': 'Services',
    'author': 'Your Name',
    'license': 'LGPL-3',
    'depends': ['base','mail','helpdesk','account'],
    'data': [
        'security/ir.model.access.csv',
        'views/custom_task_views.xml',
        'data/cron_data.xml',
        'data/mail_template_data/xml'
    ],
    'installable': True,
    'application': True,
}