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
    def __separar_montos(lista_montos: list[Monto]) -> dict[str, list[Monto]]:
        """
        Agrupa una lista de objetos Monto según su tipo de moneda.
    
        Args:
            lista_montos (list[Monto]): Lista de montos a clasificar por tipo de moneda.
    
        Returns:
            dict[str, list[Monto]]: Diccionario donde cada clave es el tipo de moneda
            (ej. "USD", "CUP") y el valor es una lista de objetos Monto correspondientes.
            Ejemplo: {"USD": [Monto(...), ...], "CUP": [Monto(...), ...]}
        """
        montos_por_moneda: dict[str, list[Monto]] = {}
    
        for monto in lista_montos:
            tipo_moneda = monto.tipo()
            if tipo_moneda not in montos_por_moneda:
                montos_por_moneda[tipo_moneda] = [monto]
            else:
                montos_por_moneda[tipo_moneda].append(monto)
    
        return montos_por_moneda
    
    @staticmethod
    def __procesar(costo: tuple[str, float], lista_montos: list[Monto]) -> dict:
        """### Procesa los montos disponibles y calcula el total convertido en la moneda objetivo.

        Args:
            costo (tuple[str, float]): Tupla con la moneda objetivo (str) y el costo requerido (float).
            lista_montos (list[Monto]): Lista de objetos Monto que representan las cantidades disponibles en distintas monedas.

        Returns:
            dict: Diccionario con la moneda objetivo, el costo requerido, el total convertido,
                    y las diferencias de sobrante o faltante respecto al costo.

        """
        moneda_objetivo: str = costo[0]   # Moneda en la que se debe pagar, ej. "CUP"
        costo_requerido: float = costo[1] # Cantidad a pagar, ej. 150.0

        montos_por_moneda: dict = Pago.__separar_montos(lista_montos)  
        # Ejemplo: {"CUP": [Monto(...), ...], "USD": [Monto(...), ...]}

        monto_total_convertido: Monto     # Resultado final en la moneda objetivo
        valores_convertidos: list[float] = []  # Lista de subtotales por cada tipo de moneda

        # Recorremos cada tipo de moneda
        for tipo_moneda in montos_por_moneda.keys():
            subtotal: float = 0.0
            if tipo_moneda == moneda_objetivo:
                for monto in montos_por_moneda[tipo_moneda]:
                    subtotal += monto.valor()
            else:
                for monto in montos_por_moneda[tipo_moneda]:
                    subtotal += monto.conversionA(moneda_objetivo)
            valores_convertidos.append(subtotal)

        # Sumamos todos los subtotales
        total_convertido: float = sum(valores_convertidos)

        monto_total_convertido = Monto(total_convertido, moneda_objetivo)
    
        sobrante = monto_total_convertido.valor() - costo_requerido
        faltante = costo_requerido - monto_total_convertido.valor()
    
        # Comparaciones
        if total_convertido > costo_requerido:
            sobrante = total_convertido - costo_requerido
            faltante = 0.0
        elif total_convertido < costo_requerido:
            sobrante = 0.0
            faltante = costo_requerido - total_convertido
        else:
            sobrante = 0.0
            faltante = 0.0

        return {
            "moneda": moneda_objetivo,
            "costo_requerido": costo_requerido,
            "total_convertido": total_convertido,
            "sobrante": sobrante,
            "faltante": faltante
        }

    @staticmethod
    def __main(args : dict)-> dict:
        pass
    
