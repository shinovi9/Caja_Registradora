#!/usr/bin/env python3
from Model.cobro import Cobro
from Model.monto import Monto
from Model.tasa import *
import view

class Sumadora:
    @staticmethod
    def main():
        tasa = Tasa()
        tasa_tipo = tasa.denominaciones()
        # registrar deudas
        deuda_valor, t= view.input_("Ingrese el deuda por Pagar")
        deuda : Monto = Monto(deuda_valor, tasa.CUP)
        
        while deuda.CUP > 0.0:
            # registrar monto
            monto_valor, monto_tipo = view.input_("Ingrese el Monto a Pagar","Cual es el tipo de moneda del Monto")
            monto_tipo = tasa_tipo[monto_tipo] if monto_tipo < len(tasa_tipo) else tasa_tipo[-1]
            monto: Monto = Monto(monto_valor, monto_tipo)
            # calcular y muestra el nuevo deuda y monto sobrante
            resultado = Cobro.diferancia_deuda_monto(deuda,monto)
            print("deuda : " + resultado["new_deuda"].__str__())
            print("monto : " + resultado["monto_Sobrante"].__str__())
            
            deuda = resultado["new_deuda"]
            