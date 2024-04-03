def mcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a

# Solicitar al usuario ingresar los valores de los números
try:
    num1 = int(input("Ingrese el primer número entero: "))
    num2 = int(input("Ingrese el segundo número entero: "))
    resultado = mcd(num1, num2)
    print(f"El MCD de {num1} y {num2} es {resultado}")
except ValueError:
    print("Por favor, ingrese valores enteros válidos.")

