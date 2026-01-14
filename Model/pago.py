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
    def __consultar_deuda(deudor : str, tipo : str = '')-> tuple:
        pass
    
    @staticmethod
    def __actualizar_deuda(dudor : str, monto_ : tuple):
        pass
    
    @staticmethod
    def __main(args : dict)-> dict:
        pass