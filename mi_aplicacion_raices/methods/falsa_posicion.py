def falsa_posicion(f, a, b, tol, max_iter=100):
    """
    Implementa el método de falsa posición para encontrar la raíz de una función f en el intervalo [a, b].

    Este método itera hasta que el error porcentual aproximado (Ea) sea menor que la tolerancia especificada (tol)
    o hasta alcanzar el número máximo de iteraciones. En cada iteración, se calcula el punto xr usando la fórmula
    de la falsa posición y se actualiza el intervalo [a, b] según el cambio de signo en f.

    Parámetros:
        f (function): Función a evaluar. Debe aceptar un número real y retornar un número real.
        a (float): Límite inferior del intervalo (valor ingresado por el usuario).
        b (float): Límite superior del intervalo (valor ingresado por el usuario).
        tol (float): Tolerancia para el error porcentual aproximado (valor ingresado por el usuario).
        max_iter (int, opcional): Número máximo de iteraciones permitidas. Por defecto es 100.

    Retorna:
        list[dict]: Lista de diccionarios, cada uno representando una iteración, con las siguientes claves:
            - "a": Valor del límite inferior en la iteración actual.
            - "b": Valor del límite superior en la iteración actual.
            - "xr": Valor estimado de la raíz en la iteración actual.
            - "fx": Valor de la función evaluado en xr.
            - "ea": Error porcentual aproximado (None en la primera iteración).

    Excepciones:
        ValueError: Si tol o max_iter no son positivos o si el intervalo [a, b] no tiene un cambio de signo.
        ZeroDivisionError: Si se produce una división por cero (por ejemplo, cuando f(a) y f(b) son iguales).
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

    iteraciones = []  # Lista para almacenar los datos de cada iteración
    xr_old = None  # Variable para almacenar el xr de la iteración anterior (para calcular el error)

    # Iterar hasta alcanzar el máximo de iteraciones
    for i in range(max_iter):
        try:
            # Evitar división por cero: si f(a) es igual a f(b), se lanza una excepción
            if f(a) == f(b):
                raise ZeroDivisionError("División por cero: f(a) y f(b) tienen el mismo valor.")

            # Calcular xr utilizando la fórmula de falsa posición:
            # xr = b - (f(b) * (a - b)) / (f(a) - f(b))
            xr = b - (f(b) * (a - b)) / (f(a) - f(b))
            fxr = f(xr)  # Evaluar la función en xr
        except ZeroDivisionError as zde:
            raise ZeroDivisionError("Error en la iteración {}: ".format(i + 1) + str(zde))
        except Exception as e:
            raise Exception("Error al evaluar la función en la iteración {}: ".format(i + 1) + str(e))

        # Calcular el error porcentual aproximado (Ea) si no es la primera iteración
        if xr_old is not None:
            try:
                ea = abs((xr - xr_old) / xr) * 100
            except ZeroDivisionError:
                ea = float('inf')
        else:
            ea = None  # No se puede calcular el error en la primera iteración

        # Registrar los valores de la iteración en la lista
        iteraciones.append({
            "a": a,
            "b": b,
            "xr": xr,
            "fx": fxr,
            "ea": ea
        })

        # Si el error calculado es menor que la tolerancia, se finaliza el proceso
        if ea is not None and ea < tol:
            break

        # Actualizar el intervalo [a, b]:
        # Si f(a)*f(xr) es negativo, la raíz se encuentra entre a y xr, se actualiza b = xr;
        # en caso contrario, se actualiza a = xr.
        try:
            if f(a) * fxr < 0:
                b = xr
            else:
                a = xr
        except Exception as e:
            raise Exception("Error al actualizar el intervalo en la iteración {}: ".format(i + 1) + str(e))

        xr_old = xr  # Guardar el valor actual para la próxima iteración

    return iteraciones
