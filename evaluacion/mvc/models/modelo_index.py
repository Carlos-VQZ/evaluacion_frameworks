class ModeloIndex:
    def __init__(self):
        pass

    def obtener_datos_index(self, nombre_usuario):
        try:
            datos = {
                'titulo': f"Bienvenido, {nombre_usuario}!",
                'mensaje': '¡Has iniciado sesión con éxito!'
            }
            return datos
        except Exception as e:
            print(f"Error al obtener datos para la página de index - {e}")
            return {}
