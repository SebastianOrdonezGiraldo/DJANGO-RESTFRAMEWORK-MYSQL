# utils/plot.py

import sympy
import matplotlib

matplotlib.use('Agg')  # Para que se ejecute en entornos sin interfaz gráfica (e.g., servidores)
import matplotlib.pyplot as plt
import numpy as np
import os


def generate_plot(func_str, a, b, root, filename='resultado.png'):
    """
    Genera un gráfico de la función en el intervalo [a, b] y marca la raíz aproximada 'root'.
    Guarda la imagen en 'static/img/filename' y retorna la ruta relativa al archivo.

    Parámetros:
        func_str (str): Cadena de texto que representa la función (ej. "x**2 - 4").
        a (float): Límite inferior del intervalo.
        b (float): Límite superior del intervalo.
        root (float): Raíz aproximada donde se marcará un punto.
        filename (str): Nombre de la imagen resultante.

    Retorna:
        str: Ruta relativa donde se guardó la imagen (por ejemplo, "static/img/resultado.png").
    """
    # Convertir la cadena en una expresión evaluable con sympy
    x = sympy.Symbol('x')
    expr = sympy.sympify(func_str)
    f = sympy.lambdify(x, expr, 'numpy')  # Usamos 'numpy' para trabajar con arrays

    # Crear un rango de valores entre a y b
    X = np.linspace(a, b, 300)
    Y = f(X)

    # Crear la figura
    plt.figure()
    plt.axhline(0, color='black', linewidth=1)  # Eje X
    plt.plot(X, Y, label='f(x)')

    # Marcar la raíz en el gráfico
    plt.plot(root, f(root), 'ro', label='Raíz aproximada')

    plt.title('Gráfica de la función')
    plt.xlabel('x')
    plt.ylabel('f(x)')
    plt.legend()

    # Ruta para guardar la imagen
    plot_path = os.path.join('static', 'img', filename)

    # Guardar la imagen y cerrar la figura
    plt.savefig(plot_path)
    plt.close()

    # Retornar la ruta relativa para usarla en la plantilla
    return plot_path
