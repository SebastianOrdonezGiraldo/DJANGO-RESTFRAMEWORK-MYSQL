from flask import Flask, render_template, request, redirect, url_for
from methods.biseccion import biseccion
from methods.falsa_posicion import falsa_posicion
from methods.punto_fijo import punto_fijo
from methods.newton_raphson import newton_raphson
from methods.secante import secante
from utils.parser import parse_function, parse_function_g, parse_derivative
from utils.plot import generate_plot


# Funciones de ayuda para parsear la función ingresada
from utils.parser import parse_function, parse_function_g, parse_derivative
# Función para generar el gráfico (debes implementarla según tus necesidades)
from utils.plot import generate_plot

app = Flask(__name__)


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/resultados", methods=["POST"])
def resultados():
    # Se extraen los datos del formulario
    metodo = request.form.get("metodo")
    funcion_input = request.form.get("funcion")
    tol = float(request.form.get("tolerancia"))
    max_iter = int(request.form.get("max_iter", 100))

    # Se definirán variables para el intervalo o aproximaciones según el método
    resultados_metodo = []
    plot_path = None  # Ruta de la imagen generada para la gráfica

    try:
        if metodo == "biseccion":
            # Se espera que el formulario tenga campos 'a' y 'b'
            a = float(request.form.get("a"))
            b = float(request.form.get("b"))
            f = parse_function(funcion_input)
            resultados_metodo = biseccion(f, a, b, tol, max_iter)
            # Genera la gráfica en el intervalo [a, b] marcando la raíz final
            plot_path = generate_plot(funcion_input, a, b, resultados_metodo[-1]["xr"])

        elif metodo == "falsa_posicion":
            a = float(request.form.get("a"))
            b = float(request.form.get("b"))
            f = parse_function(funcion_input)
            resultados_metodo = falsa_posicion(f, a, b, tol, max_iter)
            plot_path = generate_plot(funcion_input, a, b, resultados_metodo[-1]["xr"])

        elif metodo == "punto_fijo":
            # Para este método, se espera que el usuario ingrese el valor inicial 'x0'
            # y que la función ingresada sea g(x) de la forma x = g(x)
            x0 = float(request.form.get("x0"))
            g = parse_function_g(funcion_input)
            resultados_metodo = punto_fijo(g, x0, tol, max_iter)
            # Para la gráfica, se puede definir un intervalo alrededor del resultado final
            xr_final = resultados_metodo[-1]["x_new"]
            a = xr_final - 5
            b = xr_final + 5
            plot_path = generate_plot(funcion_input, a, b, xr_final)

        elif metodo == "newton_raphson":
            # Se espera que el usuario ingrese el valor inicial 'x0'
            # y también la derivada de la función en un campo 'derivada'
            x0 = float(request.form.get("x0"))
            f = parse_function(funcion_input)
            df_input = request.form.get("derivada")
            df = parse_derivative(df_input)
            resultados_metodo = newton_raphson(f, df, x0, tol, max_iter)
            xr_final = resultados_metodo[-1]["x_new"]
            a = xr_final - 5
            b = xr_final + 5
            plot_path = generate_plot(funcion_input, a, b, xr_final)

        elif metodo == "secante":
            # Se esperan dos aproximaciones iniciales: 'x0' y 'x1'
            x0 = float(request.form.get("x0"))
            x1 = float(request.form.get("x1"))
            f = parse_function(funcion_input)
            resultados_metodo = secante(f, x0, x1, tol, max_iter)
            xr_final = resultados_metodo[-1]["x_new"]
            a = xr_final - 5
            b = xr_final + 5
            plot_path = generate_plot(funcion_input, a, b, xr_final)

        else:
            # En caso de que el método no sea reconocido, se redirige a la página principal.
            return redirect(url_for("index"))
    except Exception as e:
        # En caso de error se podría enviar un mensaje al usuario o redirigir a una página de error.
        return render_template("error.html", mensaje=str(e))

    # Renderiza la plantilla de resultados pasando la tabla de iteraciones y la ruta de la gráfica.
    return render_template("resultados.html", datos=resultados_metodo, plot_path=plot_path)


if __name__ == "__main__":
    app.run(debug=True)
