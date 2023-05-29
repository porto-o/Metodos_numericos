def decimal_a_binario(numero):
    parte_entera = abs(int(numero))
    parte_decimal = abs(numero) - parte_entera

    # Convierte la parte entera a binario
    binario_entero = bin(parte_entera)[2:]

    # Convierte la parte decimal a binario
    binario_decimal = ""
    precision = 10  # Precisión para la parte decimal binaria
    for _ in range(precision):
        parte_decimal *= 2
        bit = int(parte_decimal)
        binario_decimal += str(bit)
        parte_decimal -= bit

    # Combina la parte entera y la parte decimal binarias
    binario = binario_entero
    if binario_decimal:
        binario += "." + binario_decimal

    if numero < 0:
        binario = "-" + binario

    return binario


def binario_a_decimal(binario):
    partes = binario.split(".")

    # Convierte la parte entera binaria a decimal
    parte_entera = int(partes[0], 2)

    # Convierte la parte decimal binaria a decimal
    parte_decimal = 0.0
    if len(partes) > 1:
        for i in range(len(partes[1])):
            bit = int(partes[1][i])
            parte_decimal += bit * 2**-(i+1)

    # Combina la parte entera y la parte decimal en un número decimal
    decimal = parte_entera + parte_decimal

    return decimal


# Ejemplo de uso para convertir de decimal a binario
numero_decimal = 10.625
numero_binario = decimal_a_binario(numero_decimal)
print("El número decimal", numero_decimal, "equivale a", numero_binario, "en binario.")

# Ejemplo de uso para convertir de binario a decimal
numero_binario = "1010101"
numero_decimal = binario_a_decimal(numero_binario)
print("El número binario", numero_binario, "equivale a", numero_decimal, "en decimal.")
