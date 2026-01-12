#!/usr/bin/env python3
from tasa import *

class Monto:
    def __init__(self, cantidad : float, tipo : str):
        """### Inicializacion del Monto
        Args:
            cantidad (float): Tamaño del Monto
            tipo (str): Tipo de Monto . Ejemplo(CUP,USD,...)
        ```
        self.__cantidad = cantidad if cantidad > 0 else 1
        self.__tipo = tipo if tipo in Tasa.tipos()  else "CUP"
        ```
        """
        self.__cantidad = cantidad if cantidad > 0 else 1
        self.__tipo = tipo if tipo in Tasa.tipos() else "CUP"

    def conversionA(self, tipo : str) -> float:
        """### Convierte la cantidad del monto, a la del monto deseado
        Args:
            tipo (str): Moneda que se desea convertir
        Returns:
            float: cantidad del Monto convertida
        """
        tasa_origen = Tasa.valor(self.__tipo)
        tasa_destino = Tasa.valor(tipo)       
        # convertir a la base
        cantidad_base = self.__cantidad * tasa_origen
        # convertir de la base a la moneda destino
        return cantidad_base / tasa_destino

    
    def cantidad(self) -> float:
        """### Obtener el Valor del monto
        Returns:
            float: Valor del monto
        """
        return self.__cantidad

    def tipo(self) -> str:
        """### Obtener el Tipo del monto
        Returns:
            str: el tipo de moneda
        """
        return self.__tipo
    
    def __str__(self):
        return f"{self.__cantidad} {self.__tipo}" 
    
