import web
from mvc.models.modelo_index import ModeloIndex

render = web.template.render('mvc/views/', base='layout')

class Index:
    def GET(self):
        try:
            nombre_usuario = web.cookies().get('nombre')

            if nombre_usuario:
                datos = ModeloIndex().obtener_datos_index(nombre_usuario)
                return render.index(titulo=datos['titulo'], mensaje=datos['mensaje'])
            else:
                web.seeother('/')
        except Exception as e:
            print(f"Error en GET de Index - {e.args}")
            return "Ups, algo salió mal"
