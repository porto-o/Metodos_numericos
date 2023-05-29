def richardson_extrapolation(h, f, x):
    # h: tamaño del paso
    # f: función a derivar
    # x: punto en el que se desea aproximar la derivada

    # Calcula las aproximaciones con diferentes tamaños de paso
    approx_1 = (f(x + h) - f(x)) / h
    approx_2 = (f(x + h/2) - f(x)) / (h/2)

    # Aplica la fórmula de extrapolación de Richardson
    extrapolation = (4 * approx_2 - approx_1) / 3

    return extrapolation

# Ejemplo de uso
def funcion(x):
    return x**2  # Función f(x) = x^2

punto = 900.0  # Punto en el que se desea aproximar la derivada
tamaño_paso = 0.1  # Tamaño del paso

resultado = richardson_extrapolation(tamaño_paso, funcion, punto)
print("La aproximación de la derivada en el punto", punto, "es:", resultado)
