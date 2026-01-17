from Model.monto import Monto
from Model.tasa import Tasa



deuda_cup = float(input("Ingrese la deuda: "))

deuda = Monto(deuda_cup, 'CUP')


#Verificar primero que existan las tasas de cambios 
try:
    tipos_disponibles = Tasa.tipos()
    print("Monedas disponibles:", tipos_disponibles)
    
    if not tipos_disponibles:
        print("ERROR: No hay tasas de cambio configuradas.")
        exit(1)
        
except Exception as e:
    print(f"ERROR: No se pudieron cargar las tasas: {e}")
    exit(1)

print()

while deuda.conversionA('CUP')!=0:
    tipo = input('Ingrese el tipo de moneda: ') or 'CUP'
    valor=float(input('Ingrese la cantidad: '))

    pago = Monto(valor, tipo)

    deuda = Monto((deuda.conversionA('CUP')-pago.conversionA('CUP')), 'CUP')

    print('Debes '+str(deuda))


if deuda.conversionA('CUP')==0:
    print('\n\nPago completado')