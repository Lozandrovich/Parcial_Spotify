from flask import Flask
from db import db
from routes.routes import musica_bp

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///musica.db'
db.init_app(app)

app.register_blueprint(musica_bp)

if __name__ == '__main__':
    app.run(debug=True)
