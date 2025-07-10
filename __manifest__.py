{
    'name': 'Odoo Google reCAPTCHA v3 Login',
    'version': '1.0',
    'category': 'Authentication',
    'summary': 'Adds Google reCAPTCHA v3 to the login form',
    'author': 'FPCBilgisayar',
    'depends': ['base', 'web', 'google_recaptcha'],
    'data': [
        'views/auth_recaptcha_templates.xml'
    ],
    'assets': {
        'web.assets_frontend': [
            '/auth_recaptcha/static/src/xml/recaptcha_script_component.xml',
            '/auth_recaptcha/static/src/js/recaptcha.js'
        ],
    },
    'installable': True,
    'auto_install': False,
}