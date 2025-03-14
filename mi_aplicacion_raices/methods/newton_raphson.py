def newton_raphson(f, df, x0, tol, max_iter=100):
    """
    Implementa el método de Newton-Raphson para encontrar la raíz de una función f utilizando su derivada df.

    El método utiliza la fórmula:
        x_new = x_old - f(x_old) / df(x_old)
    y repite el proceso hasta que el error porcentual aproximado (ea) sea menor que la tolerancia (tol)
    o se alcance el número máximo de iteraciones.

    Parámetros:
        f (function): Función a evaluar. Debe aceptar un número real y retornar un número real.
        df (function): Derivada de la función f. Debe aceptar un número real y retornar un número real.
        x0 (float): Valor inicial para la iteración (ingresado por el usuario).
        tol (float): Tolerancia para el error porcentual aproximado (ingresado por el usuario).
        max_iter (int, opcional): Número máximo de iteraciones permitidas. Por defecto es 100.

    Retorna:
        list[dict]: Lista de diccionarios, cada uno representando una iteración, con las siguientes claves:
            - "x_old": Valor anterior de la aproximación.
            - "x_new": Nueva aproximación calculada.
            - "f_x": Valor de f evaluado en x_new.
            - "ea": Error porcentual aproximado entre x_old y x_new (None en la primera iteración).

    Excepciones:
        ValueError: Si tol o max_iter no son positivos.
        ZeroDivisionError: Si se produce división por cero al evaluar df(x) (es decir, si df(x) = 0).
        Exception: Para otros errores que surjan durante la evaluación de f o df.
    """
    # Validar que la tolerancia y el número máximo de iteraciones sean mayores que cero.
    if tol <= 0:
        raise ValueError("La tolerancia debe ser un número positivo.")
    if max_iter <= 0:
        raise ValueError("El número máximo de iteraciones debe ser mayor que cero.")

    iteraciones = []  # Lista para almacenar los resultados de cada iteración.
    x_old = x0  # Valor inicial proporcionado por el usuario.

    # Iterar hasta alcanzar el máximo de iteraciones
    for i in range(max_iter):
        try:
            # Evaluar la función y su derivada en el valor actual.
            f_x = f(x_old)
            df_x = df(x_old)
        except Exception as e:
            raise Exception("Error al evaluar f o df en la iteración {}: {}".format(i + 1, e))

        # Verificar que la derivada no sea cero para evitar división por cero.
        if df_x == 0:
            raise ZeroDivisionError("Derivada igual a cero en la iteración {}: no se puede continuar.".format(i + 1))

        try:
            # Calcular la nueva aproximación usando la fórmula de Newton-Raphson.
            x_new = x_old - f_x / df_x
        except ZeroDivisionError as zde:
            raise ZeroDivisionError("División por cero en la iteración {}: {}".format(i + 1, zde))
        except Exception as e:
            raise Exception("Error al calcular x_new en la iteración {}: {}".format(i + 1, e))

        # Calcular el error porcentual aproximado (ea) si no es la primera iteración.
        if i == 0:
            ea = None
        else:
            try:
                # Si x_new es 0, se utiliza la diferencia absoluta para evitar división por cero.
                if x_new == 0:
                    ea = abs(x_new - x_old)
                else:
                    ea = abs((x_new - x_old) / x_new) * 100
            except ZeroDivisionError:
                ea = float('inf')

        # Registrar la iteración actual.
        iteraciones.append({
            "x_old": x_old,
            "x_new": x_new,
            "f_x": f(x_new),
            "ea": ea
        })

        # Si ya se calculó el error y es menor que la tolerancia, finaliza el proceso.
        if ea is not None and ea < tol:
            break

        # Actualizar x_old para la siguiente iteración.
        x_old = x_new

    return iteraciones


# Ejemplo de uso (modo standalone, para pruebas, no se ejecuta en la integración con el front-end):
if __name__ == "__main__":
    import math

    # Definir la función f(x) y su derivada df(x) para f(x) = x^2 - 4
    f = lambda x: x ** 2 - 4
    df = lambda x: 2 * x

    x0 = 3  # Valor inicial ingresado por el usuario
    tol = 0.001  # Tolerancia
    max_iter = 100  # Número máximo de iteraciones

    try:
        resultados = newton_raphson(f, df, x0, tol, max_iter)
        for idx, iteracion in enumerate(resultados, start=1):
            print("Iteración {}: x_old = {}, x_new = {}, f(x_new) = {}, ea = {}".format(
                idx, iteracion["x_old"], iteracion["x_new"], iteracion["f_x"], iteracion["ea"]))
    except Exception as error:
        print("Se produjo un error:", error)
