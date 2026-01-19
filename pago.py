#!/usr/bin/env python3
from monto import *
from tasa import *

""" 
LLeva y procesa los Pagos
"""
class Pago:

    @staticmethod
    def __tabla_tasa():
        """
        Crea una Tabla donde se muestra las Tasas de Cambio
        ```
            | 0 |  1  |  2  |
            |CUP| USD | EUR |
            |1.0|460.0|500.0|
        ```
        """
        tasa_tipo = Tasa.tipos()
        print(end="| ")
        [print(i, end=" | ") for i in range(len(tasa_tipo))]
        print()
        print(end="|")
        [print(t, end="|") for t in tasa_tipo]
        print()
        print(end="|")
        [print(Tasa.valor(t), end="|") for t in tasa_tipo]
        print()
    
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
    def __entradas(text_valor : str, text_tipo: str)->tuple:
        """### Proporciona una entrada de datos, aprueba de errores
        Args:
            text_valor (str): Descricion para la entrada del input valor
            text_tipo (str): Descricion para la entrada del input valor

        Returns:
            tuple:````python
            (valor : float, id_tipo : int )
            ```
        """
        valor : float
        tipo : int
        while True:
            try:
                valor = float(input(text_valor+"\n>_"))
            except ValueError:
                print("Porfavor ingrese un numero")
                continue
            break
        while True:
            try:
                tipo = int(input(text_tipo+"(ingrese el id)\n>_"))
            except ValueError:
                print("Porfavor ingrese un numero entero")
                continue
            break
        return (valor, tipo)
    
    @staticmethod
    def main():
        # Muestrar una Tabla de las Tasas de Cambio        
        Pago.__tabla_tasa()
        
        tasa_tipo = Tasa.tipos()
        # registrar costos
        costo_valor, costo_tipo = Pago.__entradas("Ingrese el costo por Paga","Cual es el tipo de moneda del Costo")
        costo_tipo = tasa_tipo[costo_tipo]
        costo : Monto = Monto(costo_valor, costo_tipo)
        
        while costo.conversionA(costo_tipo) > 0.0:
            # registrar monto
            monto_valor, monto_tipo = Pago.__entradas("Ingrese el Monto a Pagar","Cual es el tipo de moneda del Monto")
            monto_tipo = tasa_tipo[monto_tipo]
            monto: Monto = Monto(monto_valor, monto_tipo)
            # calcular y muestra el nuevo costo y monto sobrante
            resultado = Pago.__Calcular(costo,monto)
            print("costo : " + resultado["new_Costo"].__str__())
            print("monto : " + resultado["monto_Sobrante"].__str__())
            
            costo = resultado["new_Costo"]
                
        print("¡¡¡Gracias por su Compra!!!")
    
