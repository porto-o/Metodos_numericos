def regla_trapecio(f, a, b, n):
    # f: función a integrar
    # a, b: límites de integración
    # n: número de subintervalos

    h = (b - a) / n  # Tamaño del subintervalo

    # Suma de los valores de la función en los extremos de los subintervalos
    suma = f(a) + f(b)

    # Suma de los valores de la función en los puntos interiores de los subintervalos
    for i in range(1, n):
        x = a + i * h
        suma += 2 * f(x)

    # Cálculo de la aproximación de la integral
    aproximacion = (h / 2) * suma

    return aproximacion

# Ejemplo de uso
import math

def funcion(x):
    return math.sin(x)  # Función a integrar: sin(x)

a = 0  # Límite inferior de integración
b = math.pi  # Límite superior de integración
n = 100  # Número de subintervalos

resultado = regla_trapecio(funcion, a, b, n)
print("El resultado de la aproximación de la integral es:", resultado)
