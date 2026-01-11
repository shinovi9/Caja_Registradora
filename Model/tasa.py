#!/usr/bin/env python3
import json
class Tasa:
    __tasa_Cambio : dict
    
    @staticmethod
    def __init__(self):
        pass
    
    @staticmethod
    def valor(tipo : str)-> float:
        return Tasa.__tasa_Cambio[tipo]
    
    @staticmethod
    def tipo()-> tuple:
        return tuple(Tasa.__tasa_Cambio.keys())