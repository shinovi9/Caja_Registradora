class TipoInvalido(Exception):
    """Excepción para tipos de moneda no válidos"""
    def __init__(self):
        super().__init__(f"Tipo de moneda no válida")