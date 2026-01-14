#!/usr/bin/env python3
import json
from pathlib import Path

class Tasa:
    """Gestiona el Acceso de las Tasa de cambio"""
    __tasa_Cambio : dict
    
    @staticmethod
    def __cargar_Data()-> dict:
        """## Carga de la Base de Datos las Tasas de cambio 
        Returns:
            dict: La tasa de cambio
        """
        ruta = Path("./Caja_Registradora/Data/baseDatos_Tasas.json")
        if not ruta.exists():
            raise FileNotFoundError(f"No se encontró el archivo: {ruta}")
        return json.loads(ruta.read_text(encoding="utf-8"))

    
    __tasa_Cambio = __cargar_Data()
    
    @staticmethod
    def valor(tipo : str)-> float:
        """## Obtener el Valor actual de una moneda en la Tasa de canbio
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