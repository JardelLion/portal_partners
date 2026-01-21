from odoo import http


class Login(http.Controller):
    @http.route('/my_login', type='http', auth='public', website=True)
    def login_page(self, **kwargs):
        return http.request.render("todo.login")