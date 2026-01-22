#!/usr/bin/env python3
import json
from pathlib import Path

class Tasa:
    """Gestiona el Acceso de las Tasa de cambio"""
    __tasa_Cambio: dict
    
    @staticmethod
    def __cargar_Data() -> dict:
        """## Carga de la Base de Datos las Tasas de cambio 
        Returns:
            dict: La tasa de cambio
        """
        # Obtiene la ruta del directorio de tasa.py
        directorio_actual = Path(__file__).parent
        
        # Sube un nivel y luego navega a Data/...
        ruta = directorio_actual.parent / "Data" / "baseDatos_Tasas" / "Tasas.json"
        if not ruta.exists():
            raise FileNotFoundError(f"No se encontró el archivo: {ruta}")
        return json.loads(ruta.read_text(encoding="utf-8"))
    
    __tasa_Cambio = __cargar_Data()
    
    @staticmethod
    def valor(tipo: str) -> float:
        """## Obtener el Valor actual de una moneda en la Tasa de cambio
        Args:
            tipo (str): tipo de moneda
        Returns:
            float: Valor actual de la moneda
        """
        if tipo not in Tasa.__tasa_Cambio.keys():
            raise ValueError("Tipo invalido")
        return Tasa.__tasa_Cambio[tipo]
    
    @staticmethod
    def tipos() -> tuple:
        """### Obtener los Tipos de Monedas disponibles en la tasa de Cambio
        Returns:
            tuple: Todas la monedas disponibles
        """
        return tuple(Tasa.__tasa_Cambio.keys())
    


    @staticmethod
    def update(tipo: str, valor: float):
        """## Actualiza o agrega una tasa de cambio
        
        Args:
            tipo (str): Tipo de moneda (ej: 'USD', 'EUR')
            valor (float): Nuevo valor de la tasa
        """
        if not isinstance(valor, (int, float)) or valor <= 0:
            raise ValueError(f"El valor debe ser un número positivo. Se recibió: {valor}")
        
        # Actualizar el diccionario interno
        Tasa.__tasa_Cambio[tipo.upper()] = float(valor)
        print(f"✓ Tasa actualizada: {tipo.upper()} = {valor}")
    
    @staticmethod
    def save():
        """## Guarda las tasas actualizadas en el archivo JSON
        
        Este método sobrescribe el archivo Tasas.json con los valores actuales
        """
        try:
            # Obtiene la ruta del directorio de tasa.py
            directorio_actual = Path(__file__).parent
            
            # Construir la ruta al archivo JSON
            ruta = directorio_actual.parent / "Data" / "baseDatos_Tasas" / "Tasas.json"
            
            # Asegurarse de que el directorio existe
            ruta.parent.mkdir(parents=True, exist_ok=True)
            
            # Guardar con formato legible 
            ruta.write_text(
                json.dumps(Tasa.__tasa_Cambio, indent=2, ensure_ascii=False), 
                encoding="utf-8"
            )
            print("✓ Archivo Tasas.json guardado exitosamente")
            
        except Exception as e:
            raise IOError(f"No se pudo guardar el archivo: {e}")