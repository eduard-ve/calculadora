import mysql.connector
from datetime import datetime

class Database:
    def __init__(self, host="localhost", user="root", password="", database="calculadora"):
        self.host = host
        self.user = user
        self.password = password
        self.database = database
        self.conectar()

    def conectar(self):
        self.conn = mysql.connector.connect(
            host=self.host,
            user=self.user,
            password=self.password,
            database=self.database
        )
        self.cursor = self.conn.cursor()

    def crear_tabla(self):
        query = """
        CREATE TABLE IF NOT EXISTS historial (
            id INT AUTO_INCREMENT PRIMARY KEY,
            operacion VARCHAR(255) NOT NULL,
            resultado DOUBLE NOT NULL
        );
        """
        self.cursor.execute(query)
        self.conn.commit()

    def guardar_operacion(self, operacion, resultado):
        fecha = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        query = "INSERT INTO historial (operacion, resultado) VALUES (%s, %s)"
        self.cursor.execute(query, (operacion, resultado))
        self.conn.commit()

    def obtener_historial(self):
        query = "SELECT * FROM historial"
        self.cursor.execute(query)
        return self.cursor.fetchall()

    def cerrar(self):
        self.conn.close()
