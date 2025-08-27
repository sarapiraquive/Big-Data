import sys
import os

BASE_DIR = os.getcwd()
calc_path = os.path.join(BASE_DIR, 'calc')
if calc_path not in sys.path:
    sys.path.append(calc_path)

from Calculadora import Calculadora
from Calculadora import CalculadoraCientífica



while True:
    print("\nSeleccione la operación:")
    print("1. Suma")
    print("2. Resta")
    print("3. Multiplicación")
    print("4. División")
    print("5. Potencia")
    print("6. Raiz Cuadrada")
    print("7. Seno")
    print("8. Coseno")
    print("9. Tangente")
    print("10. Operacion concatenada (Suma y luego multiplicacion)")
    print("11. Salir")
    opcion = input("Ingrese el número de la operación: ")

    if opcion == "11":
        print("Saliendo...")
        break

    try:
        b=0
        if opcion in ["1", "2", "3", "4", "10"]:
            a = float(input("Ingrese el primer operando: "))
            b = float(input("Ingrese el segundo operando: "))
        elif opcion == "5":
            a = float(input("Ingrese la base: "))
            b = float(input("Ingrese el exponente: "))
        elif opcion == "6":
            a = float(input("Ingrese el número: "))
        elif opcion in ["7", "8", "9"]:
            a = float(input("Ingrese el ángulo en grados: "))
    except ValueError:
        print("Por favor ingrese valores numéricos válidos.")
        continue

    calc = Calculadora(a, b)
    calc2 = CalculadoraCientífica(a)

    if opcion == "1":
        print("\nResultado de la suma:", calc.suma())
    elif opcion == "2":
        print("\nResultado de la resta:", calc.resta())
    elif opcion == "3":
        print("\nResultado de la multiplicación:", calc.multiplicacion())
    elif opcion == "4":
        print("\nResultado de la división:", calc.division())
    elif opcion == "5":
        print("\nResultado de la potencia:", calc.potencia(b))
    elif opcion == "6":
        print("\nResultado de la raíz cuadrada:", calc.raiz_cuadrada())
    elif opcion == "7":
        print("\nResultado del seno:", calc2.seno())
    elif opcion == "8":
        print("\nResultado del coseno:", calc2.coseno())
    elif opcion == "9":
        print("\nResultado de la tangente:", calc2.tangente())
    elif opcion == "10":
        print("\nSe realizará la suma entre los valores, y luego una multiplicación entre el resultado y el primer valor ingresado.")
        print("\nOperación concatenada", calc.multiplicacion(a, calc.suma()))
    else:
        print("Opción no válida. Intente de nuevo.")

