#!/usr/bin/env python3
from Model.monto import Monto


class Cobro:
    """Clase para gestionar cálculos de deudas y pagos"""
    
    def __init__(self, deuda_inicial: Monto):
        """Inicializa un cobro con una deuda inicial"""
        self.deuda = deuda_inicial
     
    
    def ajustar_deuda(self, pago: Monto) -> Monto:
        """### Ajusta la deuda actual con un pago realizado
        Args:
            pago (Monto): Monto del pago realizado
        Returns:
            Monto: Nueva deuda actualizada
        """

        # Calcular nueva deuda
        nueva_deuda = Monto(self.deuda.CUP-pago.CUP)
        

        # Actualizar deuda actual
        self.deuda = nueva_deuda
        
        return nueva_deuda
    
          
    def completado(self) -> bool:
        """### Verifica si la deuda está completamente pagada
        Returns:
            bool: True si la deuda es menor o igual a 0
        """
        return self.deuda.CUP <= 0  