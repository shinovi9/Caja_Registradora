#!/usr/bin/env python3
from Model.monto import *
from Model.tasa import *
""" 
LLeva y procesa los Cobros
"""
class Cobro:
    
    @staticmethod
    def diferancia_deuda_monto(deuda: Monto, monto : Monto) -> dict[str , Monto]:
        """### Calcula la diferencia entre el deuda requerido y el monto entregado,
    devolviendo el nuevo deuda pendiente y el sobrante en CUP.

    Args:
        deuda (Monto): Monto que representa el deuda total a pagar.
        monto (Monto): Monto entregado por el cliente en alguna moneda.
    Returns:
        dict[str, Monto]: Diccionario con dos claves:
            - "new_deuda": deuda restante en CUP después de aplicar el Cobro.
            - "monto_Sobrante": Monto sobrante en CUP si el Cobros excede el deuda.
    """
        tasa = Tasa()
        new_deuda_valor : float = deuda.CUP - monto.CUP
        new_Monto_valor : float = monto.CUP - deuda.CUP
        new_deuda : Monto = Monto(new_deuda_valor, tasa.CUP)
        monto_Sobrante : Monto = Monto(new_Monto_valor,tasa.CUP)
        return {"new_deuda" : new_deuda , "monto_Sobrante" : monto_Sobrante}
    
    

    
