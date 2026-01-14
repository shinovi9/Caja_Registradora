#!/usr/bin/env python3
import json
from pathlib import Path
from monto import Monto
from tasa import Tasa
from _main import main
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
    def consultar_deuda(deudor : str)-> tuple:
        pass
    
    @staticmethod
    def actualizar_deuda(dudor : str, monto_ : Monto):
        pass