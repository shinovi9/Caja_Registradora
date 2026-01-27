#!/usr/bin/env python
from Model.tasa import *
from rich.console import Console
from rich.text import Text
from rich.prompt import Prompt
from rich.table import Table

console = Console() 

def input_(text_valor : str, text_tipo: str = '')->tuple:
    """### Proporciona una entrada de datos, aprueba de errores
    Args:
        text_valor (str): Descripción para la entrada del input valor
        text_tipo (str): Descripción para la entrada del input valor
    Returns:
        tuple:````python
        (valor : float, id_tipo : int )
        ```
    """
    tasa = Tasa()
    valor : float
    tipo : int
    while True:
        try:
            valor = float(Prompt.ask(text_valor+"\n>_"))
        except ValueError:
            console.print("Por favor ingrese un numero", style="bold red")
            continue
        break
    if not(text_tipo == '') :
        while True:
            try:
                tipo = int(Prompt.ask(text_tipo+"(ingrese el id)", choices=list(str(i) for i , s in enumerate(tasa.denominaciones()))))
            except ValueError:
                console.print("Por favor ingrese un numero entero", style="bold red")
                continue
            break
        return (valor, tipo)
    return (valor,'')

def refrescar():
    """### refresca la vista  de la consola 
    """
    console.clear()

def tabla_H():
    """### Crea una Tabla donde se muestra las Tasas de Cambio en horizontal
    ```
                        Tasas de Cambio                      
    ┏━━━━━━━━┳━━━━━━┳━━━━━━━━┳━━━━━━━━┳━━━━━━━━┳━━━━━━━┳━━━━━━┓
    ┃   ID   ┃  0   ┃   1    ┃   2    ┃   3    ┃   4   ┃  5   ┃
    ┡━━━━━━━━╇━━━━━━╇━━━━━━━━╇━━━━━━━━╇━━━━━━━━╇━━━━━━━╇━━━━━━┩
    │  Tipo  │ CUP  │  USD   │  EUR   │  CAD   │  GBP  │ MXN  │
    ├────────┼──────┼────────┼────────┼────────┼───────┼──────┤
    │ Valor  │ 1.0  │ 460.0  │ 500.0  │ 300.0  │ 553.0 │ 25.0 │
    └────────┴──────┴────────┴────────┴────────┴───────┴──────┘
    ```
    """
    tasa = Tasa()
    tasa_tipo = tasa.denominaciones()
    #crear tabla
    tabla = Table(title="\nTasas de Cambio", header_style= "bold cyan", border_style="bold salmon1",width=59,title_style="bold magenta3")
    
    tabla.add_column("ID", justify="center",style="bold")
    for idx in range(len(tasa_tipo)):
        tabla.add_column(str(idx),justify="center",style="bold cyan")
    tabla.add_row("Tipo",*tasa_tipo,end_section=True,style="bold magenta")
    tabla.add_row("Valor",*[str(tasa.valor(v)) for v in tasa_tipo],end_section=True,style="bold red")
    console.print(tabla,justify="center")
    
def printHeader():
    """## Imprime un Banner que dice Caja Registradora
    ```
    
⫘⫘⫷.⟬⟭⫸⫘⫘⫘⫘⫷.⟬⟭⫸⫘⫘⫘⫘⫷.⟬⟭⫸⫘⫘⫘⫘⫷.⟬⟭⫸⫘⫘⫘⫘⫷.⟬⟭⫸⫘⫘

    ____ ____  _ ____    ____ ____ ____ _ ____ ___ ____ ____ ___  ____ ____ ____
    |    |__|  | |__|    |__/ |___ | __ | [__   |  |__/ |__| |  \ |  | |__/ |__|
    |___ |  | _| |  |    |  \ |___ |__] | ___]  |  |  \ |  | |__/ |__| |  \ |  |

⫘⫘⫷.⟬⟭⫸⫘⫘⫘⫘⫷.⟬⟭⫸⫘⫘⫘⫘⫷.⟬⟭⫸⫘⫘⫘⫘⫷.⟬⟭⫸⫘⫘⫘⫘⫷.⟬⟭⫸⫘⫘
    ```
    """
    cadenas_banner = """⫘⫘⫷.⟬⟭⫸⫘⫘"""
    ascii_banner = """
____ ____  _ ____    ____ ____ ____ _ ____ ___ ____ ____ ___  ____ ____ ____ 
|    |__|  | |__|    |__/ |___ | __ | [__   |  |__/ |__| |  \\ |  | |__/ |__| 
|___ |  | _| |  |    |  \\ |___ |__] | ___]  |  |  \\ |  | |__/ |__| |  \\ |  | 
    """

    console.print("\n"+cadenas_banner*(console.width//9),style="bold red")
    console.print(ascii_banner,style="bold salmon1",justify="center")
    console.print(cadenas_banner*(console.width//9),style="bold red")

def printMonto(is_monto : str, monto__str__ : str):
    """Imprime el Monto y su datos

    Args:
        is_monto (str): Que monto es: deuda or monto 
        monto__str__ (str): Lo que retorna el método __str__ de al objeto Monto
    """
    is_monto = Text(is_monto,style="bold green")
    monto__str__ = Text(monto__str__,style="bold red")
    en = Text(" :  ",style="white")
    
    console.print(is_monto,end="")
    console.print(en,end="")
    console.print(monto__str__)
    
