def bairstow(p, tol, max_iter):
    n = len(p) - 1  # Grado del polinomio
    b = [0] * (n+1)  # Coeficientes iniciales de b
    c = [0] * (n+1)  # Coeficientes iniciales de c
    r = 0.0  # Inicializar r
    s = 0.0  # Inicializar s

    # Iteraciones hasta alcanzar la convergencia o el máximo de iteraciones
    for k in range(max_iter):
        b[-1] = p[-1]  # Asignar el último coeficiente del polinomio original a b[n]
        b[-2] = p[-2] + r*b[-1]  # Asignar el penúltimo coeficiente del polinomio original a b[n-1]

        for i in range(n-2, -1, -1):
            b[i] = p[i] + r*b[i+1] + s*b[i+2]  # Calcular los coeficientes de b

        c[-1] = b[-1]  # Asignar el último coeficiente de b a c[n]
        c[-2] = b[-2] + r*c[-1]  # Asignar el penúltimo coeficiente de b a c[n-1]

        for i in range(n-2, -1, -1):
            c[i] = b[i] + r*c[i+1] + s*c[i+2]  # Calcular los coeficientes de c

        # Actualizar los valores de r y s
        D = c[2]*c[2] + c[1]*(c[3] - c[1])
        dr = (-b[0]*c[2] + b[1]*c[1]) / D
        ds = (-b[1]*c[2] + b[0]*(c[3] - c[1])) / D
        r += dr
        s += ds

        if abs(dr) < tol and abs(ds) < tol:
            break

    return r, s

# Prueba el método de Bairstow con un polinomio de ejemplo
polinomio = [1, -6, 11, -6, 1]  # Coeficientes del polinomio
tolerancia = 1e-6
max_iteraciones = 100

r, s = bairstow(polinomio, tolerancia, max_iteraciones)
print("Las raíces aproximadas son:", r, "y", s)
