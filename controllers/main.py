from odoo import http
from odoo.http import request
from odoo.addons.web.controllers.home import Home
import requests

class AuthRecaptcha(Home):
    @http.route()
    def web_login(self, *args, **kwargs):
        if request.httprequest.method == 'POST':
            public_key = request.env['ir.config_parameter'].sudo().get_param('recaptcha_public_key')
            private_key = request.env['ir.config_parameter'].sudo().get_param('recaptcha_private_key')
            if not public_key or not private_key:
                return super(AuthRecaptcha, self).web_login(*args, **kwargs)
            
            token = kwargs.get('g-recaptcha-response')
            if not token:
                return request.render('auth_recaptcha.recaptcha_error')
            
            recaptcha_min_score = float(request.env['ir.config_parameter'].sudo().get_param('recaptcha_min_score', default='0.5'))
            r = requests.post('https://www.google.com/recaptcha/api/siteverify', data={
                'secret': private_key,
                'response': token
            })

            result = r.json()
            if not result.get('success') or result.get('score', 0) < recaptcha_min_score:
                return request.render('auth_recaptcha.recaptcha_error')

        return super(AuthRecaptcha, self).web_login(*args, **kwargs)
