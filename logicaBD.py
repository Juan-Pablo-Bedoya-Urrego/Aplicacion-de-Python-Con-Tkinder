import pyodbc
class BaseDeDatos: 
    @staticmethod   
    def agregarUsuario(nombre,contraseña):
        usuario = "Juan"
        password = "123"
        bd = "EntregaPyhton"
        ip = "localhost"
        puerto = "1433"

        cadena_conexion = (
            f"DRIVER={{ODBC Driver 17 for SQL Server}};"
            f"SERVER={ip},{puerto};"
            f"DATABASE={bd};"
            f"UID={usuario};"
            f"PWD={password};"
        )
        try:
            conn = pyodbc.connect(cadena_conexion)
            cursor = conn.cursor()
            sql = "INSERT INTO usuarios VALUES (?,?)"
            cursor.execute(sql,(nombre,contraseña))
            conn.commit()
            cursor.close()
            conn.close()
            print("Guardado")
        except Exception as e:
            print(e)
    
    @staticmethod
    def buscarUsuario(nombre,contraseña):
        usuario = "Juan"
        password = "123"
        bd = "EntregaPyhton"
        ip = "localhost"
        puerto = "1433"

        cadena_conexion = (
            f"DRIVER={{ODBC Driver 17 for SQL Server}};"
            f"SERVER={ip},{puerto};"
            f"DATABASE={bd};"
            f"UID={usuario};"
            f"PWD={password};"
        )
        try:
            conn = pyodbc.connect(cadena_conexion)
            cursor = conn.cursor()
            sql = "SELECT * FROM usuarios WHERE nombreUsuario = ? AND contraseñaUsuario = ?"
            cursor.execute(sql, (nombre, contraseña))
            resultado = cursor.fetchall()
            cursor.close()
            conn.close()
            if resultado:
                return True
            else:
                return False
        except pyodbc.Error as e:
            print("Error de base de datos:", e)
            return False
    
    @staticmethod
    def buscarNombre(nombre):
        usuario = "Juan"
        password = "123"
        bd = "EntregaPyhton"
        ip = "localhost"
        puerto = "1433"

        cadena_conexion = (
            f"DRIVER={{ODBC Driver 17 for SQL Server}};"
            f"SERVER={ip},{puerto};"
            f"DATABASE={bd};"
            f"UID={usuario};"
            f"PWD={password};")
        try:
            conn = pyodbc.connect(cadena_conexion)
            cursor = conn.cursor()
            sql = "SELECT * FROM usuarios WHERE nombreUsuario = ?"
            cursor.execute(sql, (nombre))
            resultado = cursor.fetchall()
            cursor.close()
            conn.close()
            if resultado:
                return True
            else:
                return False
        except pyodbc.Error as e:
            print("Error de base de datos:", e)
            return False
    
    @staticmethod
    def ActualizarContraseña(nombre,contraseña):
        usuario = "Juan"
        password = "123"
        bd = "EntregaPyhton"
        ip = "localhost"
        puerto = "1433"

        cadena_conexion = (
            f"DRIVER={{ODBC Driver 17 for SQL Server}};"
            f"SERVER={ip},{puerto};"
            f"DATABASE={bd};"
            f"UID={usuario};"
            f"PWD={password};")
        try:
            conn = pyodbc.connect(cadena_conexion)
            cursor = conn.cursor()
            sql = "update usuarios set contraseñaUsuario = ? where nombreUsuario = ?"
            cursor.execute(sql,(contraseña,nombre))
            conn.commit()
            cursor.close()
            conn.close()
        except Exception as e:
            print(e)