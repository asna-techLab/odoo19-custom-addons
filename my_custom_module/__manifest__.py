{
    'name': 'Custom Task Manager',
    'version': '1.0',
    'summary': 'Manage custom tasks in Odoo 19',
    'category': 'Services',
    'author': 'Your Name',
    'depends': ['base'],
    'data': [
        'security/ir.model.access.csv',
        'views/custom_task_views.xml',
    ],
    'installable': True,
    'application': True,
}