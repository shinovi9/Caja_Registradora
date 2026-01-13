# console_view.py
class View:
    def Mostrar_Menú(self):
        print("\n Menú Principal")
        print("1. Opción 1")
        print("2. Opción 2")
        print("3. Opción 3")
        
    def Opción_Seleccionada(self):
        return input("Por favor, selecciona una opción: ")

    def Mostrar_Mensaje(self, mensaje):
        print(f"\n{mensaje}")

if __name__ == "__main__":
    """## Ejecutar el código siguiente si el archivo View está siendo probado como principal(main)
    Si la clase View va a ser ejecutado desde main.py, el código a partir de aquí no se ejecuta"""
    print("Probando la Vista...")
    view = View()
    view.Mostrar_Menú()
    selección = view.Opción_Seleccionada()
    view.Mostrar_Mensaje(f"Seleccionaste: {selección}")