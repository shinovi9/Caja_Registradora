#!/usr/bin/env python3
from pathlib import Path
import json

class Tasa:
    """Gestiona el Acceso de las Tasa de cambio"""
    __tasa_Cambio : dict
    @staticmethod
    def __cargar_Data() -> dict:
        """## Carga de la Base de Datos las Tasas de cambio 
        Returns:
            dict: La tasa de cambio
        """
        # Obtiene la ruta del directorio de tasa.py
        directorio_actual = Path(__file__).parent
        
        # Sube un nivel y luego navega a Data/...
        ruta = directorio_actual.parent / "Data" / "DataBase" / "Tasas.json"
        if not ruta.exists():
            raise FileNotFoundError(f"No se encontró el archivo: {ruta}")
        return json.loads(ruta.read_text(encoding="utf-8"))
    
    def __init__(self):
        Tasa.__tasa_Cambio : dict = Tasa.__cargar_Data()

    
    def valor(self,denominacion : str) -> float:
        """## Obtener el Valor actual de una moneda en la Tasa de canbio
        Args:
            denominacion (str): denominacion de moneda
        Returns:
            float: Valor actual de la moneda
        """
        if denominacion not in Tasa.__tasa_Cambio.keys():
            raise DenominationInvalida()
        return Tasa.__tasa_Cambio[denominacion]
    
    
    def denominaciones(self) -> tuple[str]:
        """### Obtener los denominacions de Monedas disponibles en la tasa de Cambio
        Returns:
            tuple: Todas la monedas disponibles
        """
        return tuple(Tasa.__tasa_Cambio.keys())
    

    def __getattr__(self, name)-> str:
        if name not in self.denominaciones():
            raise DenominationInvalida
        return str(name)


class DenominationInvalida(Exception):
    def __init__(self):
        super().__init__(f"Denominación de moneda inválida")