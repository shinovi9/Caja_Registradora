#!/usr/bin/env python3
"""
ViewModel para el sistema de Caja Registradora.
Actúa como intermediario entre la Vista y el Modelo.
"""
#Todo: Pero el objetivo del principal del ViewModel es darle logica al View, procesar pagos es del Model porque implica logica de negocio

from Model.monto import Monto
from Model.tasa import Tasa

class ViewModel:
    """ViewModel que gestiona la lógica de procesamiento de pagos."""
    
    def __init__(self, pago_total: float = 0.0):
        """
        Inicializa el ViewModel con el pago total a completar.
        
        Args:
            pago_total (float): Monto total a pagar en CUP. Debe ser mayor que 0.
        
        Raises:
            ValueError: Si el pago_total no es un número positivo.
        """
        if not isinstance(pago_total, (int, float)) or pago_total <= 0:
            raise ValueError("El pago total debe ser un número positivo")
        
        self.__pago_total = float(pago_total)
        self.__total_pagado = 0.0  
        self.__historial_pagos = []  # Lista de objetos Monto
        self.__completado = False
    
    def procesar_pago(self, cantidad: float, tipo_moneda: str = "CUP") -> dict:
        """
        Procesa un pago realizado por el usuario.
        
        Args:
            cantidad (float): Cantidad del pago.
            tipo_moneda (str): Tipo de moneda (ej. 'CUP', 'USD').
        
        Returns:
            dict: Diccionario con los resultados del procesamiento:
                - 'exito': bool - Indica si el pago fue procesado exitosamente.
                - 'mensaje': str - Mensaje descriptivo del resultado.
                - 'pago_convertido': float - Cantidad en CUP después de conversión.
                - 'restante': float - Cantidad restante por pagar en CUP.
                - 'completado': bool - Indica si el pago total ha sido completado.
        
        Raises:
            ValueError: Si la cantidad no es positiva o el tipo de moneda no es válido.
        """
        # Validación de entrada
        if cantidad <= 0:
            raise ValueError("La cantidad debe ser un número positivo")
        
        tipos_validos = Tasa.tipos()
        if tipo_moneda not in tipos_validos:
            raise ValueError(f"Tipo de moneda no válido. Tipos aceptados: {tipos_validos}")
        
        # Crear objeto Monto con el pago
        pago = Monto(cantidad, tipo_moneda)
        
        # Convertir a CUP si es necesario
        if tipo_moneda == "CUP":
            pago_en_cup = cantidad
        else:
            pago_en_cup = pago.conversionA("CUP")
        
        # Actualizar estado
        self.__total_pagado += pago_en_cup
        self.__historial_pagos.append(pago)
        
        # Verificar si el pago está completado
        self.__completado = self.__total_pagado >= self.__pago_total
        
        # Preparar respuesta
        restante = max(0, self.__pago_total - self.__total_pagado)
        
        return {
            'exito': True,
            'mensaje': self.__generar_mensaje_pago(pago_en_cup, tipo_moneda, restante),
            'pago_convertido': pago_en_cup,
            'restante': restante,
            'completado': self.__completado
        }
    
    def __generar_mensaje_pago(self, pago_cup: float, tipo_moneda: str, restante: float) -> str:
        """
        Genera un mensaje descriptivo sobre el resultado del pago.
        
        Args:
            pago_cup (float): Pago convertido a CUP.
            tipo_moneda (str): Tipo de moneda original.
            restante (float): Cantidad restante por pagar.
        
        Returns:
            str: Mensaje formateado.
        """
        if self.__completado:
            if restante == 0:
                return "¡Pago completado exactamente! Gracias."
            else:
                cambio = -restante  # restante es negativo cuando hay exceso
                return f"¡Pago completado! Cambio: {cambio:.2f} CUP"
        else:
            return f"Pago recibido: {pago_cup:.2f} CUP ({tipo_moneda} convertido). Restante: {restante:.2f} CUP"
    
    def obtener_estado_actual(self) -> dict:
        """
        Obtiene el estado actual del proceso de pago.
        
        Returns:
            dict: Diccionario con el estado actual:
                - 'pago_total': float - Total a pagar en CUP.
                - 'total_pagado': float - Total pagado hasta ahora en CUP.
                - 'restante': float - Cantidad restante por pagar en CUP.
                - 'completado': bool - Indica si el pago está completado.
                - 'historial': list - Lista de pagos realizados.
        """
        restante = max(0, self.__pago_total - self.__total_pagado)
        
        return {
            'pago_total': self.__pago_total,
            'total_pagado': self.__total_pagado,
            'restante': restante,
            'completado': self.__completado,
            'historial': self.__historial_pagos.copy()
        }
    
    def reiniciar_pago(self, nuevo_pago_total: float = None) -> None:
        """
        Reinicia el proceso de pago, opcionalmente con un nuevo total.
        
        Args:
            nuevo_pago_total (float, optional): Nuevo total a pagar. Si es None, 
                                                mantiene el total actual.
        
        Raises:
            ValueError: Si nuevo_pago_total no es positivo.
        """
        if nuevo_pago_total is not None:
            if nuevo_pago_total <= 0:
                raise ValueError("El pago total debe ser un número positivo")
            self.__pago_total = float(nuevo_pago_total)
        
        self.__total_pagado = 0.0
        self.__historial_pagos.clear()
        self.__completado = False
    
    def obtener_tasas_disponibles(self) -> tuple:
        """
        Obtiene los tipos de monedas disponibles para pago.
        
        Returns:
            tuple: Tipos de monedas disponibles.
        """
        return Tasa.tipos()
    
    def convertir_a_cup(self, cantidad: float, tipo_moneda: str) -> float:
        """
        Convierte una cantidad de una moneda específica a CUP.
        
        Args:
            cantidad (float): Cantidad a convertir.
            tipo_moneda (str): Tipo de moneda original.
        
        Returns:
            float: Cantidad convertida a CUP.
        
        Raises:
            ValueError: Si el tipo de moneda no es válido.
        """
        if tipo_moneda not in Tasa.tipos():
            raise ValueError(f"Tipo de moneda no válido: {tipo_moneda}")
        
        if tipo_moneda == "CUP":
            return cantidad
        
        monto = Monto(cantidad, tipo_moneda)
        return monto.conversionA("CUP")
    
    @property
    def pago_total(self) -> float:
        """Obtiene el pago total en CUP."""
        return self.__pago_total
    
    @property
    def total_pagado(self) -> float:
        """Obtiene el total pagado en CUP."""
        return self.__total_pagado
    
    @property
    def completado(self) -> bool:
        """Indica si el pago ha sido completado."""
        return self.__completado
    
    @property
    def historial_pagos(self) -> list:
        """Obtiene una copia del historial de pagos."""
        return self.__historial_pagos.copy()