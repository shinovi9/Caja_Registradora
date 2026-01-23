#!/usr/bin/env python3
from Model.tasa import *

class Monto:
    def __init__(self, cantidad : float, denominacion : str = "CUP"):
        """### Inicializacion del Monto
        Args:
            cantidad (float): Tamaño del Monto
            denominacion (str): denominacion de Monto . Ejemplo(CUP,USD,...)
        """
        tasa = Tasa()
        self.__cantidad = cantidad if cantidad >= 0.0 else 0.0
        
        if denominacion in tasa.denominaciones():
            self.__denominacion = denominacion 
        else:
            raise DenominacionInvalida

    def __getattr__(self, name):
        tasa = Tasa()
        if name not in tasa.denominaciones():
            raise DenominacionInvalida
        return self.__conversionA(name)
    
    def __conversionA(self, denominacion : str) -> float:
        """### Convierte la cantidad del monto, a la del monto deseado
        Args:
            denominacion (str): Moneda que se desea convertir
        Returns:
            float: cantidad del Monto convertida
        """
        tasa = Tasa()
        tasa_origen = tasa.valor(self.__denominacion)
        tasa_destino = tasa.valor(denominacion)       
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
    def denominacion(self) -> str:
        """### Obtener el denominacion del monto
        Returns:
            str: el denominacion de moneda
        """
        return self.__denominacion
    
    def __str__(self)-> str:
        return f"{self.__cantidad} {self.__denominacion}" 
    
