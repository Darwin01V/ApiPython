from src.conexion import get_connection

class UserService:
    def __init__(self):
        self.connection = get_connection()

    def get_usuarios(self):
        try:
            cursor = self.connection.cursor()
            cursor.execute("SELECT * FROM users")
            data = cursor.fetchall()
            users = [{"id": user[0], "nombre": user[1], "apellido": user[2], "usuario": user[3]} for user in data]
            return {'error': False, 'data': users, 'msg': 'Datos obtenidos correctamente'}
        except Exception as e:
            return {'error': True, 'data': '', 'msg': f'Error al obtener los datos {e}'}

    def get_usuario(self, usuario):
        try:
            cursor = self.connection.cursor()
            cursor.execute("SELECT * FROM users WHERE usuario = %s", (usuario,))
            user = cursor.fetchone()
            if user:
                return {'error': False, 
                        'data': {"id": user[0], "nombre": user[1], "apellido": user[2], "usuario": user[3]}, 
                        'msg': 'Usuario encontrado'}
            else:
                return {'error': True, 'data': '', 'msg': 'Usuario no encontrado'}
        except Exception as e:
            return {'error': True, 'data': '', 'msg': f'Error al obtener el usuario {e}'}
