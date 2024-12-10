class View:
    @staticmethod
    def mostrar_menu():
        print("\n=== Calculadora Básica ===")
        print("1. Realizar Operación")
        print("2. Mostrar Historial")
        print("3. Salir")
        return input("Selecciona una opción: ")

    @staticmethod
    def pedir_operacion():
        operacion = input("Ingresa la operación (por ejemplo, 2 + 2 y asi con la demas operaciones): ")
        return operacion

    @staticmethod
    def mostrar_resultado(resultado):
        print(f"Resultado: {resultado}")

    @staticmethod
    def mostrar_historial(historial):
        print("\n=== Historial de Operaciones ===")
        if historial:
            for registro in historial:
                print(f"Registro: {registro}")
        else:
            print("No hay historial de operaciones.")
    @staticmethod
    def mostrar_mensaje(mensaje):
        print(mensaje)
