#!/usr/bin/env python3
from Model.monto import Monto
from Model.tasa import Tasa
from Model.cobro import Cobro

def main():
    """Función principal del programa"""
    
    print("Caja Registradora\n")
    
    # Verificar primero que existan las tasas de cambios 
    try:
        tipos_disponibles = Tasa.tipos()
        print("Monedas disponibles:", tipos_disponibles)
        
        if not tipos_disponibles:
            print("ERROR: No hay tasas de cambio configuradas.")
            exit(1)
            
    except Exception as e:
        print(f"ERROR: No se pudieron cargar las tasas: {e}")
        exit(1)
    
    # Solicitar deuda inicial
    try:
        deuda_cup = float(input("Ingrese la deuda en CUP: "))
        deuda_inicial = Monto(deuda_cup)
    except ValueError:
        print("Error: Debe ingresar un número válido para la deuda.")
        exit(1)
    
    # Crear el objeto Cobro
    cobro = Cobro(deuda_inicial)
   
    
    # Procesar pagos
    while not cobro.completado():
        
        tipo = input('\nIngrese el tipo de moneda del pago: ').upper() or 'CUP'
            
        try:
                valor_str = input('Ingrese la cantidad a pagar: ')
                valor = float(valor_str)
                if valor <= 0:
                    print("Error: La cantidad debe ser positiva.")
                    continue
        except ValueError:
                print("Error: Debe ingresar un número válido.")
                continue
            
        pago = Monto(valor, tipo)
        
        nueva_deuda = cobro.ajustar_deuda(pago)

        if(nueva_deuda.CUP>0):
           print(f"\nDebes: {nueva_deuda}")
        else:
              print("\n¡Pago completado!")
              break
                

   

if __name__ == "__main__":
    main()