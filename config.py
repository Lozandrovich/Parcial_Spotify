from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import create_engine
MYSQL_DATABASE_URI = "MySQL+pyMySQL: // root: @localhost / new conection"
engine = create_engine(MYSQL_DATABASE_URI)
try:
    with engine.connect()as concection: 
        print("La base de datos está conectada")
except Exception as e:
    print(f"error {e}")