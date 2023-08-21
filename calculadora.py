import logging

def obtener_fracciones(frac_str):
    if isinstance(frac_str, int) or isinstance(frac_str, float):
        return frac_str

    if "/" in frac_str:
        try:
            return float(frac_str)
        except ValueError:
            num, denom = frac_str.split("/")
            try:
                leading, num = num.split(" ")
                whole = float(leading)
            except ValueError:
                whole = 0
            frac = float(num) / float(denom)
            return whole - frac if whole < 0 else whole + frac
    else:
        return float(frac_str)


def sum(a, b):
    sumando_a = obtener_fracciones(a)
    sumando_b = obtener_fracciones(b)
    return sumando_a + sumando_b


def subtract(a, b):
    minuendo = obtener_fracciones(a)
    sustraendo = obtener_fracciones(b)
    return minuendo - sustraendo


def multiply(a, b):
    multiplicando = obtener_fracciones(a)
    multiplicador = obtener_fracciones(b)
    return multiplicando * multiplicador


def divide(a, b):
    dividendo = obtener_fracciones(a)
    divisor = obtener_fracciones(b)
    try:
        return dividendo / divisor
    except ZeroDivisionError:
        logging.error("Module 'calculadora.py'. División entre cero!.")
        return "Division entre cero"
