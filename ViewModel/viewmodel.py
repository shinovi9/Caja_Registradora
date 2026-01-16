#!/usr/bin/env python3
"""
ViewModel para el sistema de Caja Registradora.
Actúa como intermediario entre Vista y Modelo.
Funciones:
1. Recibir comandos de la Vista
2. Validar formato básico de entrada
3. Buscar al Modelo
4. Formatear respuestas del Modelo para la Vista
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
        self._pago_total = pago_total
    
    def procesar_entrada(self, entrada: str) -> dict:
        """
        Procesa entrada del usuario desde la Vista.
        Valida formato básico y delega al Modelo.
        
        Args:
            entrada: Formato "cantidad moneda" (ej: "100 USD")
            
        Returns:
            dict: Respuesta formateada para la Vista
        """
        try:
            # Validar formato básico
            if not entrada or not entrada.strip():
                return self._crear_error("Entrada vacía")
            
            # Parsear entrada
            partes = entrada.strip().split()
            if len(partes) != 2:
                return self._crear_error("Formato inválido. Usa: 'cantidad moneda' (ej: '100 USD')")
            
            cantidad_str, moneda = partes[0], partes[1].upper()
            
            # Validar que sea un número
            try:
                cantidad = float(cantidad_str)
            except ValueError:
                return self._crear_error(f"'{cantidad_str}' no es un número válido")
            
            # Validar que la moneda exista
            if moneda not in Tasa.tipos():
                return self._crear_error(f"Moneda '{moneda}' no aceptada. Monedas: {', '.join(Tasa.tipos())}")
            
            # Validar cantidad positiva
            if cantidad <= 0:
                return self._crear_error("La cantidad debe ser mayor que 0")
            
            # Preparar petición para el Modelo
            peticion = {
                "tipo": "registrar_pago",
                "datos": {
                    "monto": cantidad,
                    "moneda": moneda,
                    "pago_total": self._pago_total
                }
            }
            
          
            respuesta_modelo = Pago.bandeja(peticion)
            
            # Formatear respuesta para la Vista
            return self._formatear_respuesta(respuesta_modelo)
            
        except Exception as e:
            return self._crear_error(f"Error inesperado: {str(e)}")
    
    def _formatear_respuesta(self, respuesta_modelo: dict) -> dict:
        """
        Formatea la respuesta del Modelo para la Vista.
        No interpreta lógica, solo formatea presentación.
        
        Args:
            respuesta_modelo: Respuesta cruda del Modelo
            
        Returns:
            dict: Respuesta formateada para UI
        """
        if respuesta_modelo.get("error"):
            return self._crear_error(respuesta_modelo["error"])
        
        # Extraer datos del modelo
        estado = respuesta_modelo.get("estado", {})
        detalles = respuesta_modelo.get("detalles", {})
        
        # Formatear para presentación
        return {
            'exito': True,
            'estado': {
                'pago_total': f"{estado.get('pago_total', 0):.2f} CUP",
                'pagado': f"{estado.get('pagado', 0):.2f} CUP",
                'restante': f"{estado.get('restante', 0):.2f} CUP",
                'completado': estado.get('completado', False),
                'numero_pagos': estado.get('numero_pagos', 0)
            },
            'ultimo_pago': {
                'monto_ingresado': f"{detalles.get('monto_ingresado', 0):.2f} {detalles.get('moneda_ingresada', '')}",
                'monto_convertido': f"{detalles.get('monto_convertido', 0):.2f} CUP"
            },
            'cambio': f"{detalles.get('cambio', 0):.2f} CUP" if detalles.get('cambio', 0) > 0 else None,
            'mensaje': self._generar_mensaje(estado, detalles)
        }
    
    def _generar_mensaje(self, estado: dict, detalles: dict) -> str:
        """Genera mensaje descriptivo para el usuario."""
        if estado.get('completado'):
            cambio = detalles.get('cambio', 0)
            if cambio == 0:
                return "✅ Pago completado exactamente"
            else:
                return f"✅ Pago completado. Cambio: {cambio:.2f} CUP"
        else:
            restante = estado.get('restante', 0)
            monto_convertido = detalles.get('monto_convertido', 0)
            return f"📝 Recibido: {monto_convertido:.2f} CUP. Falta: {restante:.2f} CUP"
    
    def _crear_error(self, mensaje: str) -> dict:
        """Crea respuesta de error formateada."""
        return {
            'exito': False,
            'mensaje': f"❌ {mensaje}",
            'estado': None,
            'ultimo_pago': None,
            'cambio': None
        }
    
    # PROPIEDADES PARA LA VISTA 
    
    def obtener_estado_actual(self) -> dict:
        """
        Obtiene el estado actual del pago.
        Solo hace una consulta al Modelo.
        """
        peticion = {
            "tipo": "consultar_estado",
            "datos": {
                "pago_total": self._pago_total
            }
        }
        
        respuesta = Pago.bandeja(peticion)
        
        if respuesta.get("error"):
            return self._crear_error(respuesta["error"])
        
        estado = respuesta.get("estado", {})
        
        return {
            'pago_total': f"{estado.get('pago_total', 0):.2f} CUP",
            'pagado': f"{estado.get('pagado', 0):.2f} CUP",
            'restante': f"{estado.get('restante', 0):.2f} CUP",
            'completado': estado.get('completado', False),
            'numero_pagos': estado.get('numero_pagos', 0)
        }
    
    @property
    def monedas_aceptadas(self) -> list:
        """Obtiene monedas disponibles (solo consulta al Modelo)."""
        return list(Tasa.tipos())
    
    @property
    def tasas_cambio(self) -> list:
        """Obtiene tasas de cambio (solo consulta al Modelo)."""
        return [f"1 {moneda} = {Tasa.valor(moneda)} CUP" 
                for moneda in Tasa.tipos()]
    
    @property
    def completado(self) -> bool:
        """Consulta al Modelo si el pago está completado."""
        estado = self.obtener_estado_actual()
        return estado.get('completado', False)