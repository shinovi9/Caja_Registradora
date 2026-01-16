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
    def __procesar(costos: tuple, montos : list)-> dict:
        
        restante_monto : float
        tamaño_total_Monto : float
        montos_xTipos : dict
        montos_finales : list
        costos_faltante : tuple
        

        tipo_destinado = costos[0]
        tasa_destino = Tasa.valor(tipo_destinado)
        
        for monto in montos: # Separar los tipos de Monto
            if monto.tipo() not in montos_xTipos:
                montos_xTipos[monto.tipo()] = [monto,]
            else:
                montos_xTipos[monto.tipo()].append(monto)
        # Agrupacion de los montos del tipo a la deudea destinado
        if tipo_destinado in montos_xTipos:
            montos_finales = [m for m in montos_xTipos[tipo_destinado]]
        # Calculo del tamaño_total_monto
        costos_faltante : tuple = (tipo_destinado, 0.0)
        
        if len(montos_xTipos.keys()) > 1:
            pass
        else: # en caso de no tener aque convertir montos
            for vM in montos_finales:
                tamaño_total_Monto += vM.valor()            
        restante_monto = costos[1] - tamaño_total_Monto
        if restante_monto <= 0 :
            costos_faltante = (tipo_destinado, 0.0)
            if restante_monto < 0:
                restante_monto -= restante_monto*2
        elif restante_monto > 0:
            costos_faltante = (tipo_destinado, restante_monto)
        pago_exitoso = True if costos_faltante == 0.0 else False
        
        return {"pago_exitoso" : pago_exitoso ,"sobrante" : restante_monto, "faltante" : costos_faltante}
    
    @staticmethod
    def __main(args : dict)-> dict:
        pass