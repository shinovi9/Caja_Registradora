#!/usr/bin/env python3
import json
from pathlib import Path
from Model.monto import Monto
from Model.tasa import Tasa
""" 
LLeva y procesa los Pagos
"""
class Pago:
    
    @staticmethod
    def bandeja(peticion : dict):
        pass
    
    @staticmethod
    def __procesar(deudor : str, montos : list)-> dict:
        pass
    
    @staticmethod
    def consultar_Deuda(deudor : str)-> float:
        pass
    
