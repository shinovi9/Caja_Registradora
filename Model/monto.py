#!/usr/bin/env python3
from tasa import *

class Monto:
    def __init__(self, cantidad : float, tipo : str):
        """### Inicializacion del Monto
        Args:
            cantidad (float): Tamaño del Monto
            tipo (str): Tipo de Monto . Ejemplo(CUP,USD,...)
        """
        self.__cantidad = cantidad
        self.__tipo = tipo
        
    def convercionA(self, tipo : str) -> float:
        """### Convirte la cantidad del monto, a la del monto deceado
        Args:
            tipo (str): Moneda que se decea convertir
        Returns:
            float: cantidad del Monto convertida
        """
        if Tasa.valor(self.__tipo) == 1.0:
            return self.__cantidad / Tasa.valor(tipo)
        return self.__cantidad * Tasa.valor(tipo)
    
    def cantidad(self) -> float:
        """_summary_
        Returns:
            float: _description_
        """
        return self.__cantidad

    def tipo(self) -> str:
        """_summary_
        Returns:
            str: _description_
        """
        return self.__tipo
    
    def __str__(self):
        return f"{self.__cantidad} {self.__tipo}" 