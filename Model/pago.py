#!/usr/bin/env python3
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
    def __Calcular(costo: Monto, monto : Monto) -> dict[str : Monto]:
        """### Calcula la diferencia entre el costo requerido y el monto entregado,
    devolviendo el nuevo costo pendiente y el sobrante en CUP.

    Args:
        costo (Monto): Monto que representa el costo total a pagar.
        monto (Monto): Monto entregado por el cliente en alguna moneda.
    Returns:
        dict[str, Monto]: Diccionario con dos claves:
            - "new_Costo": Monto restante en CUP después de aplicar el pago.
            - "monto_Sobrante": Monto sobrante en CUP si el pago excede el costo.
    """
        new_Costo_valor : float = costo.conversionA("CUP") - monto.conversionA("CUP")
        new_Monto_valor : float = monto.conversionA("CUP") - monto.conversionA("CUP")
        new_Costo : Monto = Monto(new_Costo_valor,"CUP")
        monto_Sobrante : Monto = Monto(new_Monto_valor,"CUP")
        return {"new_Costo" : new_Costo , "monto_Sobrante" : monto_Sobrante}
    
    @staticmethod
    def __main()-> dict:
        pass
    
