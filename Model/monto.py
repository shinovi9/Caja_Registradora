#!/usr/bin/env python3
from Model.tasa import *
from Model.tipo_inválido import TipoInvalido


class Monto:
    def __init__(self, cantidad: float, tipo: str='CUP'):
        """### Inicialización del Monto
        Args:
            cantidad (float): Tamaño del Monto
            tipo (str): Tipo de Moneda 
        """
        self.__cantidad = cantidad 
        self.__tipo = tipo if tipo in Tasa.tipos() else "CUP"

    def conversionA(self, indice: int) -> float:
        """### Convierte la cantidad del monto, a la moneda en el índice especificado
        Args:
            indice (int): Índice de la moneda deseada en la lista de tipos
        Returns:
            float: cantidad del Monto convertida
        """
        # Obtener la lista de tipos
        tipos_lista = list(Tasa.tipos())
        
        # Verificar que el índice sea válido
        if indice < 0 or indice >= len(tipos_lista):
            raise ValueError(f"Índice {indice} fuera de rango. Válidos: 0 a {len(tipos_lista)-1}")
        
        # Obtener el tipo de moneda destino a partir del índice
        tipo_destino = tipos_lista[indice]
        
        # Obtener tasas de cambio
        tasa_origen = Tasa.valor(self.__tipo)
        tasa_destino = Tasa.valor(tipo_destino)
        
        # Convertir a la base (CUP)
        cantidad_base = self.__cantidad * tasa_origen
        
        # Convertir de la base a la moneda destino
        if tasa_destino != 0:
            return cantidad_base / tasa_destino
        
        raise TipoInvalido()

    @property
    def cantidad(self) -> float:
        """### Obtener el Valor del monto
        Returns:
            float: Valor del monto
        """
        return self.__cantidad
    
    @property
    def tipo(self) -> str:
        """### Obtener el Tipo del monto
        Returns:
            str: el tipo de moneda
        """
        return self.__tipo
    
    def __str__(self) -> str:
        return f"{self.__cantidad} {self.__tipo}"
    
    def __getattr__(self, name):
        """Permite acceder a la conversión como atributo: monto.CUP, monto.USD,...
        
        Mapea el nombre del atributo (tipo de moneda) a su índice y llama a conversionA con ese índice.
        Si la moneda no se encuentra, lanza TipoInvalido.
        """
        # Verificar si el nombre es un tipo de moneda válido
        if name in Tasa.tipos():
            # Obtener el índice de la moneda en la lista de tipos
            tipos_lista = list(Tasa.tipos())
            
            indice = tipos_lista.index(name)
            # Llamar a conversionA con el índice
            return self.conversionA(indice)
           
        else:
            raise TipoInvalido()
        

