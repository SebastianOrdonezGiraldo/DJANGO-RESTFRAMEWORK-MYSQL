def biseccion(f, a, b, tol, max_iter=100):
    """
    Implementa el método de bisección para encontrar la raíz de una función f en el intervalo [a, b].

    El método divide iterativamente el intervalo en dos, evaluando la función en el punto medio y
    determinando en qué subintervalo se encuentra el cambio de signo. El proceso se repite hasta que
    el error porcentual aproximado (Ea) sea menor que la tolerancia especificada o se alcance el máximo
    de iteraciones.

    Parámetros:
        f (function): Función a evaluar. Debe aceptar un número real y retornar un número real.
        a (float): Límite inferior del intervalo (ingresado por el usuario).
        b (float): Límite superior del intervalo (ingresado por el usuario).
        tol (float): Tolerancia para el error porcentual aproximado (ingresado por el usuario).
        max_iter (int, opcional): Número máximo de iteraciones permitidas. Por defecto es 100.

    Retorna:
        list[dict]: Lista de diccionarios, cada uno representando una iteración, con las siguientes claves:
            - "a": Valor del límite inferior en la iteración actual.
            - "b": Valor del límite superior en la iteración actual.
            - "xr": Valor del punto medio (estimación de la raíz) en la iteración actual.
            - "fx": Valor de la función evaluado en xr.
            - "ea": Error porcentual aproximado (None en la primera iteración).

    Excepciones:
        ValueError: Si tol o max_iter no son positivos, o si el intervalo [a, b] no presenta cambio de signo.
        Exception: Para otros errores que surjan durante la evaluación de la función o la actualización del intervalo.
    """
    # Validar que la tolerancia y el número máximo de iteraciones sean mayores que cero
    if tol <= 0:
        raise ValueError("La tolerancia debe ser un número positivo.")
    if max_iter <= 0:
        raise ValueError("El número máximo de iteraciones debe ser mayor que cero.")

    # Evaluar la función en los extremos del intervalo para verificar el cambio de signo
    try:
        fa = f(a)
        fb = f(b)
    except Exception as e:
        raise ValueError("Error al evaluar la función en los extremos del intervalo: " + str(e))

    # Verificar que f(a) y f(b) tengan signos opuestos
    if fa * fb >= 0:
        raise ValueError("La función no cambia de signo en el intervalo [a, b]. Ingrese un intervalo válido.")

    iteraciones = []  # Lista para almacenar los resultados de cada iteración
    xr_old = None    # Variable para guardar el xr de la iteración anterior (para el cálculo del error)

    # Bucle de iteración hasta alcanzar el máximo de iteraciones
    for i in range(max_iter):
        try:
            # Calcular el punto medio del intervalo actual
            xr = (a + b) / 2.0
            fxr = f(xr)  # Evaluar la función en el punto medio
        except Exception as e:
            raise Exception("Error al evaluar la función en la iteración {}: {}".format(i + 1, e))

        # Calcular el error porcentual aproximado (Ea) si no es la primera iteración
        if xr_old is not None:
            try:
                ea = abs((xr - xr_old) / xr) * 100
            except ZeroDivisionError:
                ea = float('inf')
        else:
            ea = None  # No se puede calcular el error en la primera iteración

        # Registrar la iteración actual
        iteraciones.append({
            "a": a,
            "b": b,
            "xr": xr,
            "fx": fxr,
            "ea": ea
        })

        # Si el error es menor que la tolerancia o f(xr) es cero, finalizamos el proceso
        if (ea is not None and ea < tol) or fxr == 0:
            break

        # Actualizar el intervalo según el signo de f(a) * f(xr)
        try:
            if f(a) * fxr < 0:
                b = xr
            else:
                a = xr
        except Exception as e:
            raise Exception("Error al actualizar el intervalo en la iteración {}: {}".format(i + 1, e))

        xr_old = xr  # Actualizar xr_old para la próxima iteración

    return iteraciones
