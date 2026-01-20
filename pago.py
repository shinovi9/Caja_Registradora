#!/usr/bin/env python3
from monto import *
from tasa import *
import view
""" 
LLeva y procesa los Pagos
"""
class Pago:
    
    @staticmethod
    def __Calcular(costo: Monto, monto : Monto) -> dict[str , Monto]:
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
        new_Monto_valor : float = monto.conversionA("CUP") - costo.conversionA("CUP")
        new_Costo : Monto = Monto(new_Costo_valor,"CUP")
        monto_Sobrante : Monto = Monto(new_Monto_valor,"CUP")
        return {"new_Costo" : new_Costo , "monto_Sobrante" : monto_Sobrante}
    
    
    @staticmethod
    def main():
        tasa_tipo = Tasa.tipos()
        # registrar costos
        costo_valor, costo_tipo = view.input_("Ingrese el costo por Paga","Cual es el tipo de moneda del Costo")
        costo_tipo = tasa_tipo[costo_tipo]
        costo : Monto = Monto(costo_valor, costo_tipo)
        
        while costo.conversionA(costo_tipo) > 0.0:
            # registrar monto
            monto_valor, monto_tipo = view.input_("Ingrese el Monto a Pagar","Cual es el tipo de moneda del Monto")
            monto_tipo = tasa_tipo[monto_tipo]
            monto: Monto = Monto(monto_valor, monto_tipo)
            # calcular y muestra el nuevo costo y monto sobrante
            resultado = Pago.__Calcular(costo,monto)
            print("costo : " + resultado["new_Costo"].__str__())
            print("monto : " + resultado["monto_Sobrante"].__str__())
            
            costo = resultado["new_Costo"]
                
        print("¡¡¡Gracias por su Compra!!!")
    
