def regla_simpson_tres_octavos_compuesta(f, a, b, n):
    # f: función a integrar
    # a, b: límites de integración
    # n: número de subintervalos (debe ser múltiplo de 3)

    h = (b - a) / n  # Tamaño del subintervalo

    # Suma de los valores de la función en los extremos y los puntos interiores de los subintervalos
    suma = f(a) + f(b)

    for i in range(1, n):
        x = a + i * h
        if i % 3 == 0:
            suma += 2 * f(x)
        else:
            suma += 3 * f(x)

    # Cálculo de la aproximación de la integral
    aproximacion = (3 * h / 8) * suma

    return aproximacion

# Ejemplo de uso
import math

def funcion(x):
    return math.sin(x)  # Función a integrar: sin(x)

a = 0  # Límite inferior de integración
b = math.pi  # Límite superior de integración
n = 100  # Número de subintervalos (debe ser par)

resultado = regla_simpson_tres_octavos_compuesta(funcion, a, b, n)
print("El resultado de la aproximación de la integral es:", resultado)
