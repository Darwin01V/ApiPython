from src.Service.UserService import UserService

user_service = UserService()

def get_usuarios():
    return user_service.get_usuarios()

def get_usuario(usuario):
    return user_service.get_usuario(usuario)
