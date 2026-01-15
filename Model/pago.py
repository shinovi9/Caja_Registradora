#!/usr/bin/env python3
import json
from pathlib import Path
from monto import Monto
from tasa import Tasa

""" 
LLeva y procesa los Pagos
"""
class Pago:
    
    @staticmethod
    def bandeja(peticion : dict)-> dict:
        pass
    
    @staticmethod
    def __procesar(deudor : str, montos : list)-> dict:
        pass
    
    @staticmethod
    def __consultar_deuda(deudor : str, tipo : str = ''):
        """### Optiene la informacion de las deudas  

        Args:
            deudor (str): Persona que debe el dinero
            tipo (str, optional): Moneda de la Deuda. Defaults to ''.
        Raises:
            FileNotFoundError: Si no se encuentra el archivo Deudores.json
        Returns:
        tuple:
            - Si no se encuentra el Deudor → (deudor, 0)
            - Si se especifica el tipo → (tipo, monto_de_la_deuda)
            - Si no, se devuelve todas las deudas → (deuda,)
        """
        deuda : dict
        ruta = Path("./Caja_Registradora/Data/baseDatos_Deuda/Deudores.json")
        
        if not ruta.exists():
            raise FileNotFoundError(f"No se encontró el archivo: {ruta}")
        
        with open(ruta, "r", encoding="utf-8") as f:
            data = json.load(f)
            if deudor not in data:
                return (deudor,0)
            deuda = data[deudor]
            
        if tipo and tipo in deuda :
            return (tipo, deuda[tipo])
        return (deuda,)
        
    @staticmethod
    def __actualizar_deuda(dudor : str, monto_ : tuple):
        pass
    
    @staticmethod
    def __main(args : dict)-> dict:
        pass