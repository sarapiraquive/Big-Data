"""
Herramientas de Big Data – Taller HBD: Implementación de Calculadora (OOP)

Estudiantes: Sebastian Castellanos 275012, Gabriel Jimenez 244428, Sara Piraquive 274348
Carrera: Ingeniería Informática / Analítica Aplicada
Universidad de La Sabana – Maestría en Analítica Aplicada
Profesor: Hugo Franco, Ph.D.
Fecha: 25 de agosto de 2025

1. Nombre o tarea del punto del Taller
Implementación de una calculadora básica–científica en Python empleando Programación Orientada a Objetos (POO).

1.1. Breve descripción del problema
Se requiere diseñar e implementar una calculadora que ejecute operaciones aritméticas básicas (suma, resta, multiplicación, división, potencia y raíz cuadrada) y funciones científicas (seno, coseno, tangente). El diseño debe tener manejo de errores de entrada (p.ej., división por cero, tipos no numéricos). El objetivo es demostrar el uso de clases, métodos y encapsulamiento en Python para automatizar cálculos y favorecer la reutilización del código.

1.2. Método de solución
• Enfoque: Programación Orientada a Objetos (POO) con dos clases:
  – Calculadora: encapsula estado (operando1, operando2, operacion) y provee operaciones básicas: suma, resta, multiplicacion, division, potencia, raiz_cuadrada. Incluye utilitario actualizaOperandos y representación __str__.
  – CalculadoraCientífica: hereda de Calculadora y añade seno, coseno y tangente.
• Datos/Variables: No hay datasets externos. Variables internas tipo float/int. Se maneja ZeroDivisionError y TypeError con mensajes al usuario.
• Modelado: estado mutable; cada método retorna self para permitir encadenamiento (chaining). El resultado numérico queda en self.operando1.

Algoritmo 1. Operación aritmética (pseudocódigo)

función/procedimiento operacion_binaria(operando1, operando2, símbolo, operador):
    this.operacion ← símbolo
    this.actualizaOperandos(operando1, operando2)
    intentar:
        this.operando1 ← operador(this.operando1, this.operando2)
        retornar this
    capturar TypeError:
        imprimir "El operando debe ser numérico"
        retornar None

Algoritmo 2. División (pseudocódigo, caso especial)

función division(operando1, operando2):
    this.operacion ← "/"
    this.actualizaOperandos(operando1, operando2)
    intentar:
        this.operando1 ← this.operando1 / this.operando2
        retornar this
    capturar ZeroDivisionError:
        imprimir "No se puede dividir por cero"
        retornar None
    capturar TypeError:
        imprimir "El operando debe ser numérico"
        retornar None

Algoritmo 3. Funciones científicas (unarias)

función trigonométrica(nombre, f):
    this.operacion ← nombre  # "sin", "cos" o "tan"
    intentar:
        this.operando1 ← f(this.operando1)
        retornar this
    capturar TypeError:
        imprimir "El operando debe ser numérico"
        retornar None

Luego, se implementa el método en Python (ver código a continuación) que sigue esta estructura, usando la librería estándar math.

1.3. Resultados (ejecución y salidas)
Para ejecutar ejemplos, ejecute este archivo directamente (ver bloque __main__). Ejemplos:
- Suma 8 + 5 → resultado = 13
- División 10 / 0 → mensaje de error y resultado None
- Potencia 2 ** 3 → resultado = 8
- Seno(π/2) → ≈ 1.0
Las figuras no aplican; se reporta salida por consola e impresión del estado de la calculadora. 

1.4. Discusión
El diseño con herencia separa claramente operaciones básicas y científicas, facilitando la extensión (p.ej., logaritmos). El manejo explícito de errores mejora la robustez para entradas no válidas. El retorno self permite encadenar operaciones, aunque requiere comprender que el resultado muta en operando1. Como mejora futura, podría añadirse un método resultado() inmutable o un historial de operaciones.

Referencias
No se emplearon fuentes externas; se siguieron las especificaciones del Taller HBD provistas en el PDF del curso.
"""
