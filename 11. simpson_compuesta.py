def regla_simpson_compuesta(f, a, b, n):
    # f: función a integrar
    # a, b: límites de integración
    # n: número de subintervalos (debe ser par)

    h = (b - a) / n  # Tamaño del subintervalo

    suma = f(a) + f(b)  # Suma de los valores en los extremos

    # Suma de los valores en los puntos interiores de los subintervalos
    for i in range(1, n):
        x = a + i * h
        if i % 2 == 0:
            suma += 2 * f(x)
        else:
            suma += 4 * f(x)

    # Cálculo de la aproximación de la integral
    aproximacion = (h / 3) * suma

    return aproximacion

# Ejemplo de uso
import math

def funcion(x):
    return math.sin(x)  # Función a integrar: sin(x)

a = 0  # Límite inferior de integración
b = math.pi  # Límite superior de integración
n = 100  # Número de subintervalos (debe ser par)

resultado = regla_simpson_compuesta(funcion, a, b, n)
print("El resultado de la aproximación de la integral es:", resultado)
