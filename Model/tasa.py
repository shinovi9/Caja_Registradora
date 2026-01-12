#!/usr/bin/env python3
import json

class Tasa:

    __tasa_Cambio : dict
    
    @staticmethod
    def __cargar_Data():
        """## Carga de la Base de Datos las Tasas de cambio 
        Returns:
            dict: La tasa de cambio
        """
        tasa : dict
        with open("./Caja_Registradora/Data/baseDatos_Tasas.json","r") as db_Tasas:
            tasa = json.load(db_Tasas)
        return tasa
    
    __tasa_Cambio = __cargar_Data()
    
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
    def tipos()-> tuple:
        """### Obtener los Tipos de Monedas disponibles en la tasa de Cambio
        Returns:
            tuple: Todas la monedas disponibles
        """
        return tuple(Tasa.__tasa_Cambio.keys())