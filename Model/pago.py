#!/usr/bin/env python3
from monto import Monto
from tasa import Tasa

""" 
LLeva y procesa los Pagos
"""
class Pago:
    
    @staticmethod
    def bandeja():
        Pago.__main()

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
    def __main():
        # Muestrar una Tabla de las Tasas de Cambio
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
        costo_valor : float
        costo_tipo : str
        monto_valor : float
        monto_tipo : str
        while True:
            try:
                costo_valor = float(input("Ingrese el costo por Pagar\n>_"))
            except ValueError:
                print("Porfavor ingrese un numero")
                continue
            break
        while True:
            try:
                costo_tipo = int(input("Cual es el tipo de moneda del Costo(ingrese el id)\n>_"))
            except ValueError:
                print("Porfavor ingrese un numero entero")
                continue
            break
        costo_tipo = tasa_tipo[costo_tipo]

        costo : Monto = Monto(costo_valor, costo_tipo)
        while costo.conversionA(costo_tipo) > 0.0:
            while True:
                try:
                    monto_valor = float(input("Ingrese el Monto a Pagar\n>_"))
                except ValueError:
                    print("Porfavor ingrese un numero")
                    continue
                break
            while True:
                try:
                    monto_tipo = int(input("Cual es el tipo de moneda del Monto(ingrese el id)\n>_"))
                except ValueError:
                    print("Porfavor ingrese un numero entero")
                    continue
                break
            monto_tipo = tasa_tipo[monto_tipo]
            monto: Monto = Monto(monto_valor, monto_tipo)
            
            resultado = Pago.__Calcular(costo,monto)
            print("costo : " + resultado["new_Costo"].__str__())
            print("monto : " + resultado["monto_Sobrante"].__str__())
            costo = resultado["new_Costo"]
        print("¡¡¡Gracias por su Compra!!!")
    
