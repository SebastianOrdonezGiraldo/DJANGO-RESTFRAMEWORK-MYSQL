def punto_fijo(g, x0, tol, max_iter=100):
    """
    Implementa el método de punto fijo para encontrar una solución de la ecuación x = g(x).

    El método itera la función g partiendo de un valor inicial x0, calculando el siguiente valor:
        x_new = g(x_old)
    y repitiendo el proceso hasta que la diferencia entre dos iteraciones consecutivas (error aproximado)
    sea menor que la tolerancia tol, o se alcance el número máximo de iteraciones.

    Parámetros:
        g (function): Función iterativa, g(x), donde se espera que la solución cumpla x = g(x).
        x0 (float): Valor inicial para la iteración (ingresado por el usuario).
        tol (float): Tolerancia para el error aproximado (ingresado por el usuario).
        max_iter (int, opcional): Número máximo de iteraciones permitidas. Por defecto es 100.

    Retorna:
        list[dict]: Lista de diccionarios, cada uno representando una iteración, con las siguientes claves:
            - "x_old": Valor de la iteración anterior.
            - "x_new": Valor calculado para la nueva iteración mediante g(x_old).
            - "ea": Error porcentual aproximado entre x_old y x_new (None en la primera iteración).

    Excepciones:
        ValueError: Si tol o max_iter no son positivos.
        Exception: Para errores que surjan durante la evaluación de la función g en alguna iteración.
    """
    # Validar que la tolerancia y el número máximo de iteraciones sean mayores que cero.
    if tol <= 0:
        raise ValueError("La tolerancia debe ser un número positivo.")
    if max_iter <= 0:
        raise ValueError("El número máximo de iteraciones debe ser mayor que cero.")

    iteraciones = []  # Lista para almacenar los resultados de cada iteración.
    x_old = x0  # Se asigna el valor inicial.

    # Bucle para realizar las iteraciones del método de punto fijo.
    for i in range(max_iter):
        try:
            # Evaluar la función iterativa g en el valor anterior.
            x_new = g(x_old)
        except Exception as e:
            raise Exception("Error al evaluar la función g en la iteración {}: {}".format(i + 1, e))

        # Calcular el error porcentual aproximado (ea) si no es la primera iteración.
        if i == 0:
            ea = None  # No se puede calcular el error en la primera iteración.
        else:
            try:
                # Si x_new es 0, se usa la diferencia absoluta para evitar división por cero.
                if x_new == 0:
                    ea = abs(x_new - x_old)
                else:
                    ea = abs((x_new - x_old) / x_new) * 100
            except ZeroDivisionError:
                ea = float('inf')

        # Registrar la iteración actual en la lista.
        iteraciones.append({
            "x_old": x_old,
            "x_new": x_new,
            "ea": ea
        })

        # Si ya se calculó un error y este es menor que la tolerancia, se detiene el proceso.
        if ea is not None and ea < tol:
            break

        # Actualizar x_old para la siguiente iteración.
        x_old = x_new

    return iteraciones


# Ejemplo de uso (para pruebas en modo standalone, no se ejecuta en la integración con el frontend):
if __name__ == "__main__":
    # Definir la función iterativa g(x). Por ejemplo, para la ecuación x = cos(x) se puede usar:
    import math

    g = lambda x: math.cos(x)
    x0 = 0.5  # Valor inicial ingresado por el usuario
    tol = 0.001  # Tolerancia
    max_iter = 100  # Número máximo de iteraciones

    try:
        resultados = punto_fijo(g, x0, tol, max_iter)
        for idx, iteracion in enumerate(resultados, start=1):
            print("Iteración {}: x_old = {}, x_new = {}, ea = {}".format(
                idx, iteracion["x_old"], iteracion["x_new"], iteracion["ea"]))
    except Exception as error:
        print("Se produjo un error:", error)
