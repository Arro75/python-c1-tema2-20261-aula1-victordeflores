"""
Enunciado:
Desarrolla una aplicación web básica con Flask que responda a una petición GET y devuelva una pequeña página web.
La aplicación debe tener el siguiente endpoint:

1. `GET /greet/<nombre>`: Devuelve una página web que saluda al usuario cuyo nombre se pasa como parámetro en la URL.

Tu tarea es completar la implementación de la función create_app() y del endpoint solicitado.
Además, debes crear una plantilla HTML utilizando Jinja2 que reciba una variable `nombre` y la utilice para mostrar un mensaje de saludo.

Nota: Asegúrate de incluir una estructura HTML válida en la plantilla.
"""

from flask import Flask, render_template_string

# Implementa la plantilla HTML aquí
TEMPLATE = """
p<!doctype html>
<html>
<head>
    <meta charset="UTF-8">
    <title>Saludo Personal</title>
    <style>    
      body {
        font-family: Arial, sans-serif;
        display: flex;
        justify-content: center;
        align-items: center;
        height: 100vh;
        margin: 0;
        background-color: #f0f0f0;
      }
      .greeting {
        text-align: center;
        padding: 20px;
        background-color: white;
        border-radius: 10px;
        box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
      }
      h1 {
        color: #333;
        margin-bottom: 10px;
      }
   </style>
<head>
<body>
    <div class="greeting">
      <h1>Hola, {{ victor }}!</h1>
      <p>¡Bienvenido a nuestra página web.</p>
    </div>
<body>
</html>
"""


def create_app():
    """
    Crea y configura la aplicación Flask
    """
    app = Flask(__name__)

    @app.route('/greet/<nombre>')
    def greet(nombre):
        """
        Devuelve una página web que saluda al usuario utilizando una plantilla Jinja2
        """
        # Utiliza render_template_string para renderizar la plantilla con el nombre proporcionado:

        pass
        return render_template_string(TEMPLATE, nombre=nombre)

    return app

if __name__ == '__main__':
    app = create_app()
    app.run(debug=True)
