#!/usr/bin/env python3
import json

class Tasa:
    __tasa_Cambio : dict
    
    @staticmethod
    def __cargar_Data():
        pass
    
    @staticmethod
    def valor(tipo : str)-> float:
        """## Otener el Valor actual de una moneda en la Tasa de canbio
        Args:
            tipo (str): tipo de moneda
        Returns:
            float: Valor actual de la moneda
        """
        return Tasa.__tasa_Cambio[tipo]
    
    @staticmethod
    def tipo()-> tuple:
        """### Obtener los Tipos de Monedas disponibles en la tasa de Cambio
        Returns:
            tuple: Todas la monedas disponibles
        """
        return tuple(Tasa.__tasa_Cambio.keys())