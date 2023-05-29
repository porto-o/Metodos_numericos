def funcion(x):
    # Define aquí tu función no lineal
    return x**2 - 4

def derivada(x):
    # Define aquí la derivada de tu función no lineal
    return 2 * x

def newton_raphson(aprox_inicial, tolerancia, max_iteraciones):
    x = aprox_inicial
    iteracion = 0

    while True:
        if iteracion == max_iteraciones:
            print("El método no converge después de", max_iteraciones, "iteraciones.")
            break

        f_x = funcion(x)
        f_prime_x = derivada(x)

        if abs(f_prime_x) < tolerancia:
            print("La derivada es muy pequeña, no se puede continuar con el método.")
            break

        x_nuevo = x - f_x / f_prime_x

        if abs(x_nuevo - x) < tolerancia:
            print("Se ha alcanzado la convergencia después de", iteracion, "iteraciones.")
            break

        x = x_nuevo
        iteracion += 1

    return x

# Prueba el método de Newton-Raphson con valores de ejemplo
aprox_inicial = 2.0
tolerancia = 1e-6
max_iteraciones = 100

solucion = newton_raphson(aprox_inicial, tolerancia, max_iteraciones)
print("La solución aproximada es:", solucion)
