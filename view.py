#!/usr/bin/env python
from Model.tasa import *
from rich.console import Console
from rich.table import Table

def tabla():
    """### Crea una Tabla donde se muestra las Tasas de Cambio
    ```
            Tasas de Cambio
    ┏━━━━━┳━━━━━━┳━━━━━━━┓
    ┃ ID  ┃ Tipo ┃ Valor ┃
    ┡━━━━━╇━━━━━━╇━━━━━━━┩
    │  0  │ CUP  │  1.0  │
    ├─────┼──────┼───────┤
    │  1  │ USD  │ 460.0 │
    ├─────┼──────┼───────┤
    │  2  │ EUR  │ 500.0 │
    └─────┴──────┴───────┘
    ```
    """
    tasa = Tasa()
    tasa_tipo = tasa.denominaciones()
    console = Console()
    #crear tabla
    tabla = Table(title="Tasas de Cambio", header_style= "bold green", border_style="bold salmon1",width=22)
    #Definir Columnas
    tabla.add_column("ID", justify="center",style="bold cyan")
    tabla.add_column("Tipo", justify="center",style="bold magenta")
    tabla.add_column("Valor", justify="center",style="bold red3")
    # agregar filas a tabla
    for idx,tipo in enumerate(tasa_tipo):
        tabla.add_row(str(idx), tipo, str(tasa.valor(tipo)),end_section=True)
    # imprimir tabla
    console.print(tabla)

def input_(text_valor : str, text_tipo: str = '')->tuple:
    """### Proporciona una entrada de datos, aprueba de errores
    Args:
        text_valor (str): Descricion para la entrada del input valor
        text_tipo (str): Descricion para la entrada del input valor
    Returns:
        tuple:````python
        (valor : float, id_tipo : int )
        ```
    """
    console = Console()
    valor : float
    tipo : int
    while True:
        try:
            valor = float(input(text_valor+"\n>_"))
        except ValueError:
            console.print("Porfavor ingrese un numero", style="bold red")
            continue
        break
    if not(text_tipo == '') :
        while True:
            try:
                tipo = int(input(text_tipo+"(ingrese el id)\n>_"))
            except ValueError:
                console.print("Porfavor ingrese un numero entero", style="bold red")
                continue
            break
        return (valor, tipo)
    return (valor,'')


def refescar():
    """### refesca la vista  de la consola 
    """
    console = Console()
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
    console = Console()
    tasa_tipo = tasa.denominaciones()
    #crear tabla
    tabla = Table(title="Tasas de Cambio", header_style= "bold cyan", border_style="bold salmon1",width=59)
    
    tabla.add_column("ID", justify="center",style="bold green")
    for idx in range(len(tasa_tipo)):
        tabla.add_column(str(idx),justify="center",style="bold cyan")
    tabla.add_row("Tipo",*tasa_tipo,end_section=True,style="bold magenta")
    tabla.add_row("Valor",*[str(tasa.valor(v)) for v in tasa_tipo],end_section=True,style="bold red3")
    console.print(tabla)