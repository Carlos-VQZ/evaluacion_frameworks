import web
from mvc.models.modelo_login import UsuarioModel
from mvc.models.modelo_index import ModeloIndex

render = web.template.render('mvc/views/', base='layout')

class Login:
    def GET(self):
        return render.login()

    def POST(self):
        try:
            data = web.input()
            username = data.username
            password = data.password
            if self.validar_credenciales(username, password):
                web.setcookie('nombre', username, expires="", domain=None, secure=False)

                web.seeother('/index')
            else:
                return "Credenciales incorrectas. Inténtalo de nuevo."
                web.seeother('/')

        except Exception as e:
            print(f"Error en POST - {e}")
            return "Ups, algo salió mal."

    def validar_credenciales(self, username, password):
        usuarios = UsuarioModel().get_usuarios()
        for usuario in usuarios:
            if usuario['username'] == username and usuario['password'] == password:
                return True
        return False
