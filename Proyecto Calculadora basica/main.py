from modelo.modelo import Database
from vista.vista import View
from controlador.controlador import Controlador

def main():
    # Configurar la conexión con MySQL
    model = Database(host="localhost", user="root", password="")
    view = View()

    # Crear tabla si no existe
    model.crear_tabla()

    # Iniciar el controlador
    controlador = Controlador(model, view)  # Crear una instancia y asignarla a 'controlador'
    controlador.ejecutar()

    # Cerrar la conexión a la base de datos
    model.cerrar()

if __name__ == "__main__":
    main()