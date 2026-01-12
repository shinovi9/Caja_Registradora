#!/usr/bin/env python3
"""
ViewModel para el sistema de Caja Registradora.
Funciones:
1. Conectar Vista y Modelo
2. Recibir comandos de la Vista
3. Formatear datos del Modelo para la Vista
"""

from Model.monto import Monto
from Model.tasa import Tasa


class ViewModel:
    """ViewModel que actúa como puente entre Vista y Modelo."""
    
    def __init__(self, pago_total: float):
        """
        Inicializa el ViewModel.
        
        Args:
            pago_total (float): Monto total a pagar en CUP.
        """
    
        self._pago_total_cup = pago_total
        self._total_pagado_cup = 0.0
        self._historial_montos = []  
        self._completado = False
    
    def procesar_pago(self, cantidad: float, moneda: str) -> dict:
        """
        Procesa un pago desde la Vista.
        
        Args:
            cantidad: Cantidad ingresada por el usuario
            moneda: Tipo de moneda ingresada
            
        Returns:
            dict: Datos formateados para mostrar en la Vista
        """
        # 1. Validar moneda 
        if moneda not in Tasa.tipos():
            return self._formatear_error(f"Moneda {moneda} no aceptada")
        
        # 2. Crear objeto Monto
        monto = Monto(cantidad, moneda)
        
        # 3. Convertir a CUP
        monto_cup = monto.conversionA("CUP")
        
        # 4. Actualizar estado 
        self._total_pagado_cup += monto_cup
        self._historial_montos.append(monto)
        
        # 5. Verificar si el pago ha sido completado
        self._completado = self._total_pagado_cup >= self._pago_total_cup
        
        # 6. Formatear respuesta para la Vista
        return self._formatear_respuesta(monto, monto_cup)
    
    def _formatear_respuesta(self, monto: Monto, monto_cup: float) -> dict:
        """
        Formatea los datos del Modelo para la Vista.
        
        Args:
            monto: Objeto Monto del Modelo
            monto_cup: Valor convertido a CUP
            
        Returns:
            dict: Datos listos para mostrar en la Vista
        """
        restante = max(0, self._pago_total_cup - self._total_pagado_cup)
        
        # Generar mensaje 
        if self._completado:
            if restante == 0:
                mensaje = "✅ Pago completado exactamente"
            else:
                cambio = self._total_pagado_cup - self._pago_total_cup
                mensaje = f"✅ Pago completado. Cambio: {cambio:.2f} CUP"
        else:
            mensaje = f"📝 Recibido: {monto_cup:.2f} CUP. Falta: {restante:.2f} CUP"
        
        return {
            'monto_ingresado': str(monto),
            'monto_convertido': monto_cup,
            'total_pagado': self._total_pagado_cup,
            'restante': restante,
            'completado': self._completado,
            'mensaje': mensaje
        }
    
    def _formatear_error(self, mensaje_error: str) -> dict:
        """
        Formatea errores para la Vista.
        
        Args:
            mensaje_error: Descripción del error
            
        Returns:
            dict: Error formateado
        """
        return {
            'error': True,
            'mensaje': f"❌ {mensaje_error}",
            'completado': False
        }
    
    #PROPIEDADES DE CONSULTA PARA LA VISTA
    
    @property
    def pago_total(self) -> float:
        """Pago total para mostrar en Vista."""
        return self._pago_total_cup
    
    @property
    def total_pagado(self) -> float:
        """Total pagado para mostrar en Vista."""
        return self._total_pagado_cup
    
    @property
    def completado(self) -> bool:
        """Estado de completitud para Vista."""
        return self._completado
    
    @property
    def historial(self) -> list:
        """Historial formateado para Vista."""
        return self._historial_montos.copy()
    
    @property
    def monedas_aceptadas(self) -> list:
        """Monedas disponibles del Modelo."""
        return list(Tasa.tipos())