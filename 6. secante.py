def funcion(x):
    # Define aquí tu función
    return x**2 - 4

def secante(aprox_inicial_1, aprox_inicial_2, tolerancia, max_iteraciones):
    x0 = aprox_inicial_1
    x1 = aprox_inicial_2
    iteracion = 0

    while True:
        if iteracion == max_iteraciones:
            print("El método no converge después de", max_iteraciones, "iteraciones.")
            break

        f_x0 = funcion(x0)
        f_x1 = funcion(x1)

        if abs(f_x1 - f_x0) < tolerancia:
            print("Se ha alcanzado la convergencia después de", iteracion, "iteraciones.")
            break

        x_nuevo = x1 - f_x1 * (x1 - x0) / (f_x1 - f_x0)

        if abs(x_nuevo - x1) < tolerancia:
            print("Se ha alcanzado la convergencia después de", iteracion, "iteraciones.")
            break

        x0 = x1
        x1 = x_nuevo
        iteracion += 1

    return x_nuevo

# Prueba el método de la secante con valores de ejemplo
aprox_inicial_1 = 1.0
aprox_inicial_2 = 3.0
tolerancia = 1e-6
max_iteraciones = 100

solucion = secante(aprox_inicial_1, aprox_inicial_2, tolerancia, max_iteraciones)
print("La solución aproximada es:", solucion)
