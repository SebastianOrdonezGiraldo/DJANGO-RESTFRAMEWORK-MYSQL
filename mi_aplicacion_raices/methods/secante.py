def secante(f, x0, x1, tol, max_iter=100):
    """
    Implementa el método de la secante para encontrar la raíz de una función f utilizando dos aproximaciones iniciales.

    El método utiliza la fórmula:
        x_new = x1 - f(x1) * (x1 - x0) / (f(x1) - f(x0))
    y repite el proceso iterativo hasta que el error porcentual aproximado (ea) sea menor que la tolerancia (tol)
    o se alcance el número máximo de iteraciones.

    Parámetros:
        f (function): Función a evaluar. Debe aceptar un número real y retornar un número real.
        x0 (float): Primera aproximación inicial para la raíz (ingresada por el usuario).
        x1 (float): Segunda aproximación inicial para la raíz (ingresada por el usuario).
        tol (float): Tolerancia para el error porcentual aproximado (ingresada por el usuario).
        max_iter (int, opcional): Número máximo de iteraciones permitidas. Por defecto es 100.

    Retorna:
        list[dict]: Lista de diccionarios, cada uno representando una iteración, con las siguientes claves:
            - "x0": Primera aproximación usada en la iteración.
            - "x1": Segunda aproximación usada en la iteración.
            - "x_new": Nueva aproximación calculada.
            - "f_x_new": Valor de f evaluado en x_new.
            - "ea": Error porcentual aproximado entre x_new y x1 (None en la primera iteración).

    Excepciones:
        ValueError: Si tol o max_iter no son positivos.
        ZeroDivisionError: Si se produce una división por cero en la fórmula (cuando f(x1) - f(x0) es 0).
        Exception: Para otros errores que surjan durante la evaluación de la función f.
    """
    # Validar que la tolerancia y el número máximo de iteraciones sean positivos.
    if tol <= 0:
        raise ValueError("La tolerancia debe ser un número positivo.")
    if max_iter <= 0:
        raise ValueError("El número máximo de iteraciones debe ser mayor que cero.")

    iteraciones = []  # Lista para almacenar los resultados de cada iteración

    # Iterar hasta alcanzar el máximo de iteraciones
    for i in range(max_iter):
        try:
            f_x0 = f(x0)
            f_x1 = f(x1)
        except Exception as e:
            raise Exception("Error al evaluar la función en la iteración {}: {}".format(i + 1, e))

        # Verificar que el denominador no sea cero para evitar división por cero.
        if f_x1 - f_x0 == 0:
            raise ZeroDivisionError("División por cero en la iteración {}: f(x1) - f(x0) = 0".format(i + 1))

        try:
            # Calcular la nueva aproximación usando la fórmula de la secante.
            x_new = x1 - f_x1 * (x1 - x0) / (f_x1 - f_x0)
        except ZeroDivisionError as zde:
            raise ZeroDivisionError("División por cero al calcular x_new en la iteración {}: {}".format(i + 1, zde))
        except Exception as e:
            raise Exception("Error al calcular x_new en la iteración {}: {}".format(i + 1, e))

        # Calcular el error porcentual aproximado (ea) si no es la primera iteración.
        if i == 0:
            ea = None  # No se puede calcular el error en la primera iteración.
        else:
            try:
                # Si x_new es 0, se utiliza la diferencia absoluta para evitar división por cero.
                if x_new == 0:
                    ea = abs(x_new - x1)
                else:
                    ea = abs((x_new - x1) / x_new) * 100
            except ZeroDivisionError:
                ea = float('inf')

        # Registrar la iteración actual.
        iteraciones.append({
            "x0": x0,
            "x1": x1,
            "x_new": x_new,
            "f_x_new": f(x_new),
            "ea": ea
        })

        # Si se puede calcular el error y es menor que la tolerancia, finalizar el proceso.
        if ea is not None and ea < tol:
            break

        # Actualizar las aproximaciones para la siguiente iteración:
        # Se asigna a x0 el valor actual de x1 y a x1 el valor de x_new.
        x0, x1 = x1, x_new

    return iteraciones


# Ejemplo de uso (modo standalone, para pruebas)
if __name__ == "__main__":
    import math

    # Definir la función f(x), por ejemplo: f(x) = x**2 - 4
    f = lambda x: x ** 2 - 4

    # Aproximaciones iniciales ingresadas por el usuario.
    x0 = 0
    x1 = 3
    tol = 0.001
    max_iter = 100

    try:
        resultados = secante(f, x0, x1, tol, max_iter)
        for idx, iteracion in enumerate(resultados, start=1):
            print("Iteración {}: x0 = {}, x1 = {}, x_new = {}, f(x_new) = {}, ea = {}".format(
                idx,
                iteracion["x0"],
                iteracion["x1"],
                iteracion["x_new"],
                iteracion["f_x_new"],
                iteracion["ea"]
            ))
    except Exception as error:
        print("Se produjo un error:", error)
