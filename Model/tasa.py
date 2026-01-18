#!/usr/bin/env python3

class Tasa:
    """Gestiona el Acceso de las Tasa de cambio"""
    __tasa_Cambio : dict = {"CUP" : 1.0, "USD" : 460.0,"EUR" : 500.00,}

    @classmethod
    def valor(cls,tipo : str)-> float:
        """## Obtener el Valor actual de una moneda en la Tasa de canbio
        Args:
            tipo (str): tipo de moneda
        Returns:
            float: Valor actual de la moneda
        """
        if tipo not in Tasa.__tasa_Cambio.keys():
            raise ValueError("Tipo invalido")
        return Tasa.__tasa_Cambio[tipo]
    
    @classmethod
    def tipos(cls)-> tuple[str]:
        """### Obtener los Tipos de Monedas disponibles en la tasa de Cambio
        Returns:
            tuple: Todas la monedas disponibles
        """
        return tuple(Tasa.__tasa_Cambio.keys())