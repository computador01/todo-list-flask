from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy


# create the extension
db = SQLAlchemy()



def create_app():

    app = Flask(__name__)
    
    # Configuracion del proyecto
    app.config.from_mapping(
        DEBUG = False,
        SECRET_KEY = 'devtodo',
        SQLALCHEMY_DATABASE_URI = "sqlite:///todolist.db"
    )
    
    db.init_app(app)
    
    
    # Registrar Bluprint
    from . import todo
    app.register_blueprint(todo.bp)
    
    from . import auth
    app.register_blueprint(auth.bp)


    @app.route('/')
    def index():
        return render_template('index.html')
    
    # Permite migrar todos los modelos que vamos a crear a nuesatra base de datos
    # Si es que falta migrar. 
    with app.app_context():
        db.create_all()
    
    
    return app