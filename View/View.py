import shutil
import textwrap

def _limpiar_pantalla():
    """Borra la pantalla para que se vea limpio en el celular."""
    print("\n" * 50)

def _obtener_ancho():
    """Calcula el ancho de la pantalla actual para adaptar el texto."""
    try:
        return shutil.get_terminal_size().columns
    except:
        return 40 # Ancho seguro para móviles si falla la detección

def mostrar_titulo(titulo="CAJA REGISTRADORA"):
    """Muestra el título del programa adaptado al ancho de la pantalla."""
    width = _obtener_ancho()
    sep = "=" * width
    texto_centrado = titulo.center(width)
    
    print(sep)
    print(texto_centrado)
    print(sep)

def pedir_precios_productos():
    """
    Pide el precio de cada artículo uno por uno.
    Pregunta si es el último. Si el usuario escribe 0.00, termina.
    
    Returns:
        list[float]: Una lista con todos los precios (crudos, sin sumar).
    """
    precios = []
    
    while True:
        try:
            entrada = input("Ingrese el precio del producto (en CUP) o 0.00 para terminar: ")
            precio = float(entrada)
            
            # El usuario escribe 0.00 para terminar
            if precio == 0.00:
                break
            
            precios.append(precio)
            
            # Preguntamos si quiere agregar más
            continuar = input("¿Eso es toda la compra? (s=No, Enter=Sí): ").strip().lower()
            
            # Si escribe 's', salimos del loop. Si presiona Enter, seguimos.
            if continuar == 's':
                break
                
        except ValueError:
            print("❌ Por favor ingrese un número válido.")
            
    return precios

def mostrar_precio_total(total: float):
    """
    Muestra el total ya calculado.
    
    Args:
        total (float): El número que alguien (ViewModel/Main) calculó sumando la lista.
    """
    width = _obtener_ancho()
    texto = f"TOTAL A PAGAR: {total:.2f} CUP"
    
    print("-" * width)
    print(texto)
    print("-" * width)

def mostrar_tasas(lista_tasas: list):
    """
    Muestra la lista de tasas de cambio que le pasan.
    
    Args:
        lista_tasas (list): Lista de strings (ej: ["1 USD = 300 CUP", ...]).
    """
    print("\n--- TASAS DE CAMBIO ---")
    for tasa in lista_tasas:
        # Ajustamos el texto para que no se salga de la pantalla del celular
        print(textwrap.fill(tasa, width=_obtener_ancho()))
    print("-----------------------")

def ingresar_pago():
    """
    Pide el pago en formato 'cantidad moneda'.
    
    Returns:
        str: El texto exacto que escribió el usuario (ej: "100 USD").
    """
    pago = input("Ingrese pago (Ej: '50 USD'): ").strip()
    return pago

def pago_completado():
    """
    Muestra mensaje de éxito y pregunta si quiere hacer otra operación.
    
    Returns:
        str: 's' si quiere otra operación, cualquier otra cosa si quiere salir.
    """
    print("\n✅ PAGADO COMPLETAMENTE")
    print("Gracias por su compra.")
    
    respuesta = input("¿Desea realizar otra operación? (s/n): ").strip().lower()
    return respuesta