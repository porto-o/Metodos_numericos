def funcion(x):
    # Define aquí tu función
    return x**3 - x - 1

def muller(aprox_inicial_1, aprox_inicial_2, aprox_inicial_3, tolerancia, max_iteraciones):
    x0 = aprox_inicial_1
    x1 = aprox_inicial_2
    x2 = aprox_inicial_3
    iteracion = 0

    while True:
        if iteracion == max_iteraciones:
            print("El método no converge después de", max_iteraciones, "iteraciones.")
            break

        f_x0 = funcion(x0)
        f_x1 = funcion(x1)
        f_x2 = funcion(x2)

        h0 = x1 - x0
        h1 = x2 - x1

        delta0 = (f_x1 - f_x0) / h0
        delta1 = (f_x2 - f_x1) / h1

        a = (delta1 - delta0) / (h1 + h0)
        b = a * h1 + delta1
        c = f_x2

        discriminante = (b**2 - 4 * a * c) ** 0.5

        if abs(b - discriminante) > abs(b + discriminante):
            denominador = b - discriminante
        else:
            denominador = b + discriminante

        x_nuevo = x2 - (2 * c) / denominador

        if abs(x_nuevo - x2) < tolerancia:
            print("Se ha alcanzado la convergencia después de", iteracion, "iteraciones.")
            break

        x0 = x1
        x1 = x2
        x2 = x_nuevo
        iteracion += 1

    return x_nuevo

# Prueba el método de Müller con valores de ejemplo
aprox_inicial_1 = 0.5
aprox_inicial_2 = 1.0
aprox_inicial_3 = 1.5
tolerancia = 1e-6
max_iteraciones = 100

solucion = muller(aprox_inicial_1, aprox_inicial_2, aprox_inicial_3, tolerancia, max_iteraciones)
print("La solución aproximada es:", solucion)
