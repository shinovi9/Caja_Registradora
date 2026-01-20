#!/usr/bin/env python
from tasa import Tasa

def tabla():
    """### Crea una Tabla donde se muestra las Tasas de Cambio
    ```
        | 0 |  1  |  2  |
        |CUP| USD | EUR |
        |1.0|460.0|500.0|
    ```
    """
    tasa_tipo = Tasa.tipos()
    print(end="| ")
    [print(i, end=" | ") for i in range(len(tasa_tipo))]
    print()
    print(end="|")
    [print(t, end="|") for t in tasa_tipo]
    print()
    print(end="|")
    [print(Tasa.valor(t), end="|") for t in tasa_tipo]
    print()

def input_(text_valor : str, text_tipo: str)->tuple:
    """### Proporciona una entrada de datos, aprueba de errores
    Args:
        text_valor (str): Descricion para la entrada del input valor
        text_tipo (str): Descricion para la entrada del input valor
    Returns:
        tuple:````python
        (valor : float, id_tipo : int )
        ```
    """
    valor : float
    tipo : int
    while True:
        try:
            valor = float(input(text_valor+"\n>_"))
        except ValueError:
            print("Porfavor ingrese un numero")
            continue
        break
    while True:
        try:
            tipo = int(input(text_tipo+"(ingrese el id)\n>_"))
        except ValueError:
            print("Porfavor ingrese un numero entero")
            continue
        break
    return (valor, tipo)