# utils/parser.py

import sympy

def parse_function(func_str):
    """
    Convierte la cadena de texto 'func_str' en una función evaluable f(x).
    Uso típico: f(x) = x**2 - 4
    """
    x = sympy.Symbol('x')
    expr = sympy.sympify(func_str)  # Convierte el string en una expresión simbólica
    f = sympy.lambdify(x, expr, 'math')
    return f

def parse_function_g(func_str):
    """
    Convierte la cadena de texto 'func_str' en la función g(x) para el método de punto fijo.
    Uso típico: x = g(x).
    Ejemplo: g(x) = cos(x).
    """
    x = sympy.Symbol('x')
    expr = sympy.sympify(func_str)
    g = sympy.lambdify(x, expr, 'math')
    return g

def parse_derivative(deriv_str):
    """
    Convierte la cadena de texto 'deriv_str' en la derivada df(x).
    Uso típico: si f(x) = x**2 - 4, entonces deriv_str = "2*x".
    """
    x = sympy.Symbol('x')
    expr = sympy.sympify(deriv_str)
    df = sympy.lambdify(x, expr, 'math')
    return df
