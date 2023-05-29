def regla_punto_medio(f, a, b, n):
    # f: función a integrar
    # a, b: límites de integración
    # n: número de subintervalos

    h = (b - a) / n  # Tamaño del subintervalo

    suma = 0.0

    # Calcular la suma de los valores de la función evaluados en el punto medio de cada subintervalo
    for i in range(n):
        x = a + (i + 0.5) * h  # Punto medio del subintervalo
        suma += f(x)

    # Calcular la aproximación de la integral
    aproximacion = h * suma

    return aproximacion

# Ejemplo de uso
import math

def funcion(x):
    return math.sin(x)  # Función a integrar: sin(x)

a = 0  # Límite inferior de integración
b = math.pi  # Límite superior de integración
n = 100  # Número de subintervalos

resultado = regla_punto_medio(funcion, a, b, n)
print("El resultado de la aproximación de la integral es:", resultado)
