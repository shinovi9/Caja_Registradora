#!/usr/bin/env python3
"""
ViewModel para el sistema de Caja Registradora.
Actúa como intermediario entre Vista y Modelo.
Funciones:
1. Recibir comandos de la Vista
2. Buscar al Modelo para lógica de negocio
3. Formatear datos del Modelo para la Vista
"""

from Model.tasa import Tasa
from Model.pago import Pago


class ViewModel:
    """ViewModel que coordina la comunicación entre la vista y el modelo"""
    
    def __init__(self, pago_total: float):
        """
        Inicializa el ViewModel.
        
        Args:
            pago_total (float): Monto total a pagar en CUP.
        """
        # Crear instancia del Modelo Pago
        self._pago = Pago(pago_total)
    
    def procesar_entrada(self, entrada: str) -> dict:
        """
        Procesa entrada del usuario desde la Vista.
        Delega toda la lógica de negocio al Modelo.
        
        Args:
            entrada: Formato "cantidad moneda" (ej: "100 USD")
            
        Returns:
            dict: Datos formateados para la Vista
        """
        try:
            # Parsear entrada 
            cantidad_str, moneda = self._parsear_entrada(entrada)
            cantidad = float(cantidad_str)
            
    
            resultado_modelo = self._pago.registrar_pago(cantidad, moneda)
            
            # Formatear respuesta del Modelo para la Vista
            return self._formatear_para_vista(resultado_modelo)
            
        except ValueError as e:
            return self._crear_error(f"Error: {e}")
        except Exception as e:
            return self._crear_error(f"Error inesperado: {e}")
    
    def _parsear_entrada(self, entrada: str) -> tuple:
        """
        Parsea la entrada del usuario.
        
        Args:
            entrada: Cadena de entrada
            
        Returns:
            tuple: (cantidad_str, moneda)
        """
        entrada = entrada.strip()
        if not entrada:
            raise ValueError("Entrada vacía")
        
        partes = entrada.split()
        if len(partes) != 2:
            raise ValueError("Formato: 'cantidad moneda' (ej: '100 USD')")
        
        return partes[0], partes[1].upper()
    
    def _formatear_para_vista(self, resultado_modelo: dict) -> dict:
        """
        Formatea los datos del Modelo para presentación en Vista.
        
        Args:
            resultado_modelo: Datos crudos del Modelo
            
        Returns:
            dict: Datos formateados para UI
        """
        monto = resultado_modelo['monto_original']
        
    
        return {
            'exito': True,
            'monto_ingresado': str(monto),
            'monto_convertido': f"{resultado_modelo['monto_cup']:.2f} CUP",
            'total_acumulado': f"{resultado_modelo['total_acumulado']:.2f} CUP",
            'restante': f"{resultado_modelo['restante']:.2f} CUP",
            'completado': resultado_modelo['completado'],
            'mensaje': self._generar_mensaje(resultado_modelo)
        }
    
    def _generar_mensaje(self, resultado: dict) -> str:
        """Genera mensaje para el usuario."""
        if resultado['completado']:
            if resultado['exceso'] == 0:
                return "✅ Pago completado exactamente"
            else:
                return f"✅ Pago completado. Cambio: {resultado['exceso']:.2f} CUP"
        else:
            return f"📝 Recibido: {resultado['monto_cup']:.2f} CUP. Falta: {resultado['restante']:.2f} CUP"
    
    def _crear_error(self, mensaje: str) -> dict:
        """Crea respuesta de error formateada."""
        return {
            'exito': False,
            'mensaje': f"❌ {mensaje}",
            'completado': False
        }
    
    #PROPIEDADES PARA LA VISTA
    
    @property
    def estado_actual(self) -> dict:
        """Obtiene estado formateado para la Vista."""
        estado = self._pago.obtener_estado()
        
        return {
            'pago_total': f"{estado['total_objetivo']:.2f} CUP",
            'pagado': f"{estado['total_acumulado']:.2f} CUP",
            'restante': f"{estado['restante']:.2f} CUP",
            'completado': estado['completado'],
            'numero_pagos': estado['numero_pagos'],
            'historial': [
                f"{monto} → {monto.conversionA('CUP'):.2f} CUP"
                for monto in estado['pagos']
            ]
        }
    
    @property
    def monedas_aceptadas(self) -> list:
        """Obtiene monedas disponibles formateadas para Vista."""
        return [f"{moneda}" for moneda in Tasa.tipos()]
    
    @property
    def tasas_cambio(self) -> list:
        """Obtiene tasas de cambio formateadas para Vista."""
        return [f"1 {moneda} = {Tasa.valor(moneda):.2f} CUP" 
                for moneda in Tasa.tipos()]
    
    @property
    def completado(self) -> bool:
        """Indica si el pago está completado."""
        return self._pago.completado