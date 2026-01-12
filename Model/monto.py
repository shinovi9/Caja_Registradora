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
        tasa_origen = Tasa.valor(self.__tipo)
        tasa_destino = Tasa.valor(tipo)       
        # Paso 1: convertir a la base
        cantidad_base = self.__cantidad * tasa_origen
        # Paso 2: convertir de la base a la moneda destino
        return cantidad_base / tasa_destino

    
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
    
