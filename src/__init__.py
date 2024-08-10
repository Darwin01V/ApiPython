from flask import Flask
from src.routes import api_bp 

def create_app():
    app = Flask(__name__)
    
    # Configurar la base de datos
    app.config.from_object('src.config.Config')
    
    # Registrar rutas
    app.register_blueprint(api_bp)
    
    return app


