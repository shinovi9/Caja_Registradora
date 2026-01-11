#!/usr/bin/env python3

class Monto:
    def __init__(self, cantidad : float, tipo : str):
        """
        Docstring para __init__
        
        :param self: Descripción
        :param cantidad: Cantidad del Monto
        :type cantidad: float 
        :param tipo: tipo de Monto
        :type tipo: str
        """
        self.__cantidad = cantidad
        self.__tipo = tipo
        
    def convertir(self, tipo : str):
        pass