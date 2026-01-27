#!/usr/bin/env python3
from Model.tasa import *

class Monto:
    def __init__(self, cantidad : float, denomination : str = "CUP"):
        """### Constructor Monto
        Args:
            cantidad (float): Tamaño del Monto
            denomination (str): denomination de Monto . Ejemplo(CUP,USD,...)
        """
        tasa = Tasa()
        self.__cantidad = cantidad if cantidad >= 0.0 else 0.0
        
        if denomination in tasa.denominaciones():
            self.__denomination = denomination 
        else:
            raise DenominationInvalida

    def __getattr__(self, name):
        tasa = Tasa()
        if name not in tasa.denominaciones():
            raise DenominationInvalida
        return self.__conversionA(name)
    
    def __conversionA(self, denomination : str) -> float:
        """### Convierte la cantidad del monto, a la del monto deseado
        Args:
            denomination (str): Moneda que se desea convertir
        Returns:
            float: cantidad del Monto convertida
        """
        tasa = Tasa()
        tasa_origen = tasa.valor(self.__denomination)
        tasa_destino = tasa.valor(denomination)       
        # convertir a la base
        if self.__cantidad == 0:
            return 0.0
        cantidad_base = self.__cantidad * tasa_origen
        # convertir de la base a la moneda destino
        return cantidad_base / tasa_destino

    @property
    def valor(self) -> float:
        """### Obtener el Valor del monto
        Returns:
            float: Valor del monto
        """
        return float(self.__cantidad)
    
    @property
    def denomination(self) -> str:
        """### Obtener el denomination del monto
        Returns:
            str: el denomination de moneda
        """
        return self.__denomination
    
    def __str__(self)-> str:
        return f"{self.__cantidad} {self.__denomination}" 
    
