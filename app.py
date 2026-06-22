import os

from flask import Flask

from configuracion import Configuracion
from routes import registrar_rutas


def crear_aplicacion(configuracion_prueba=None):
    aplicacion = Flask(
        __name__,
        template_folder="templates",
        static_folder="static",
    )
    aplicacion.config.from_object(Configuracion)

    if configuracion_prueba:
        aplicacion.config.update(configuracion_prueba)

    registrar_rutas(aplicacion)
    return aplicacion


aplicacion = crear_aplicacion()


if __name__ == "__main__":
    puerto_render = int(os.environ.get("PORT", aplicacion.config["PUERTO"]))
    aplicacion.run(
        host=aplicacion.config["SERVIDOR"],
        port=puerto_render,
        debug=aplicacion.config["DEPURACION"],
    )
