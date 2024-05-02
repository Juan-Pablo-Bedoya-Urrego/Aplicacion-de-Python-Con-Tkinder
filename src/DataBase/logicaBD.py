import pyodbc
from tkinter import messagebox
class BaseDeDatos: 
    usuario = "Juan"
    password = "123"
    bd = "EntregaPyhton"
    ip = "localhost"
    puerto = "1433"

    global Conexion 
    Conexion = (
        f"DRIVER={{ODBC Driver 17 for SQL Server}};"
        f"SERVER={ip},{puerto};"
        f"DATABASE={bd};"
        f"UID={usuario};"
        f"PWD={password};"
    )
    @staticmethod
    def deleteVeto(placa):
        try:
            conn = pyodbc.connect(Conexion)
            cursor = conn.cursor()
            sql = "delete from placasVetadas where placa = ?"
            cursor.execute(sql,(placa))
            conn.commit()
            cursor.close()
            conn.close()
            messagebox.showinfo('Veto quitado' , 'El veto fue quitado con exito')
        except Exception as e:
            print(e)
    
    @staticmethod
    def agregarVeto(placa):
        try:
            conn = pyodbc.connect(Conexion)
            cursor = conn.cursor()
            sql = "INSERT INTO placasVetadas VALUES (?)"
            cursor.execute(sql,(placa))
            conn.commit()
            cursor.close()
            conn.close()
            print("Guardado")
        except Exception as e:
            print(e)
    
    @staticmethod
    def retornarVetadas():
        try:
            conn = pyodbc.connect(Conexion)
            cursor = conn.cursor()
            sql = "select placa from placasVetadas"
            cursor.execute(sql)
            placas = []
            for fila in cursor:
                placas.append(fila[0])
            conn.commit()
            cursor.close()
            conn.close()
            return placas
        except Exception as e:
            print(e)
    
    @staticmethod
    def eliminarVehiculo(placa,tipo):
        try:
            conn = pyodbc.connect(Conexion)
            cursor = conn.cursor()
            if tipo == "Moto":
                sql = "delete from moto where placa = ?"
                cursor.execute(sql, (placa))
            if tipo == "Carro":
                sql = "delete from carro where placa = ?"
                cursor.execute(sql, (placa))
            conn.commit()
            filas_afectadas = cursor.rowcount
            cursor.close()
            conn.close()
            return filas_afectadas > 0 
        except Exception as e:
            print(e)
    
    @staticmethod
    def agregarVehiculo(placa,nombre,tipo):
        try:
            conn = pyodbc.connect(Conexion)
            cursor = conn.cursor()
            if tipo == "Moto":
                sql = "INSERT INTO moto VALUES (?,?)"
                cursor.execute(sql, (placa, nombre))
            if tipo == "Carro":
                sql = "INSERT INTO carro VALUES (?,?)"
                cursor.execute(sql, (placa, nombre))
            conn.commit()
            cursor.close()
            conn.close()
            print("Guardado")
        except Exception as e:
            print(e)
    
    @staticmethod
    def buscarVehiculo(placa,tipo):
        try:
            conn = pyodbc.connect(Conexion)
            cursor = conn.cursor()
            if tipo == "Moto":
                sql = "select * from moto where placa = ?"
                cursor.execute(sql,(placa))
            if tipo == "Carro":
                sql = "select * from carro where placa = ?"
                cursor.execute(sql,(placa))
            resultado = cursor.fetchall()
            cursor.close()
            conn.close()
            if resultado:
                for resul in resultado:
                    id, placaBD, nombre = resul
                    messagebox.showinfo('Encontrada', f"La {tipo} fue encontrada con placas {placaBD}, propietario: {nombre}")
            else:
                messagebox.showerror('No encontrada', f"La {tipo} con placas {placa} no se encontro")
        except Exception as e:
            print(e)
    
    @staticmethod   
    def agregarUsuario(nombre,contraseña):
        try:
            conn = pyodbc.connect(Conexion)
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
        try:
            conn = pyodbc.connect(Conexion)
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
        try:
            conn = pyodbc.connect(Conexion)
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
        try:
            conn = pyodbc.connect(Conexion)
            cursor = conn.cursor()
            sql = "update usuarios set contraseñaUsuario = ? where nombreUsuario = ?"
            cursor.execute(sql,(contraseña,nombre))
            conn.commit()
            cursor.close()
            conn.close()
        except Exception as e:
            print(e)