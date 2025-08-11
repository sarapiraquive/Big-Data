"""
Created on Wed Aug 2, 2025
@author: Hugo Franco
"""

import math


class Calculadora:
    """
    Implementa una calculadora
    """

    tipo='cientifica'
    
    def __init__(self,operando1=0, operando2=0, operacion=None):
        self.operando1=operando1
        self.operando2=operando2
        self.operacion=operacion

    def __str__(self):
        if self.operacion is None:
            return "Calculadora en espera"
        if self.operacion in ["√", "sin", "cos", "tan"]:
            return f"{self.operacion}({self.operando1})"
        return f"{self.operando1}{self.operacion}{self.operando2}"
    
    def actualizaOperandos(self, operando1, operando2):
        if operando1 is not None:
            self.operando1 = operando1
        if operando2 is not None:
            self.operando2 = operando2
    
    def suma(self, operando1=None, operando2=None):
        self.operacion="+"
        self.actualizaOperandos(operando1, operando2)
        try:
            self.operando1 = self.operando1 + self.operando2
            return self.operando1
        except TypeError:
            print('El operando debe ser numérico')
            return None
        
    def resta(self, operando1=None, operando2=None):
        self.operacion="-"
        self.actualizaOperandos(operando1, operando2)
        try:
            self.operando1 = self.operando1 - self.operando2
            return self.operando1
        except TypeError:
            print('El operando debe ser numérico')
            return None
    
    def multiplicacion(self, operando1=None, operando2=None):
        self.operacion="*"
        self.actualizaOperandos(operando1, operando2)
        try:
            self.operando1 = self.operando1 * self.operando2
            return self.operando1
        except TypeError:
            print('El operando debe ser numérico')
            return None
    
    def division(self, operando1=None, operando2=None):
        self.operacion="/"
        self.actualizaOperandos(operando1, operando2)
        try:
            self.operando1 = self.operando1 / self.operando2
            return self.operando1
        except ZeroDivisionError:
            print('No se puede dividir por cero')
            return None
        except TypeError:
            print('El operando debe ser numérico')
            return None
        
    def potencia(self, exponente):
        self.operacion=f"**{exponente}"
        try:
            self.operando1 = self.operando1 ** exponente
            return self.operando1
        except TypeError:
            print('El operando debe ser numérico')
            return None
    
    def raiz_cuadrada(self):
        self.operacion="√"
        try:
            self.operando1 = math.sqrt(self.operando1)
            return self.operando1
        except TypeError:
            print('El operando debe ser numérico')
            return None
        
class CalculadoraCientífica(Calculadora):

    def seno(self):
        self.operacion="sin"
        try:
            self.operando1 = math.sin(self.operando1)
            return self.operando1
        except TypeError:
            print('El operando debe ser numérico')
            return None
        
    def coseno(self):
        self.operacion="cos"
        try:
            self.operando1 = math.cos(self.operando1)
            return self.operando1
        except TypeError:
            print('El operando debe ser numérico')
            return None
        
    def tangente(self):
        self.operacion="tan"
        try:
            self.operando1 = math.tan(self.operando1)
            return self.operando1
        except TypeError:
            print('El operando debe ser numérico')
            return None    


