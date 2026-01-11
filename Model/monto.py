#!/usr/bin/env python3

class Monto:
    def __init__(self, cantidad : float, tipo : str):
        """Inicializacion del Monto

        Args:
            cantidad (float): Tamaño del Monto
            tipo (str): Tipo de Monto . Ejemplo(CUP,USD,...)
        """
        self.__cantidad = cantidad
        self.__tipo = tipo
        
    def convertir(self, tipo : str):
        pass
    
    
    def cantidad(self):
        return self.__cantidad


    def tipo(self):
        return self.__tipo
    
    
    def __str__(self):
        return f"{self.__cantidad} {self.__tipo}" 