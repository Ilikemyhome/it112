from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///cars.db'

tables = SQLAlchemy()
tables.init_app(app) 

class Dream_Cars(tables.Model):
    __tablename__ = 'dream_cars'
    id = tables.Column('car_id', tables.Integer, primary_key=True)
    make = tables.Column(tables.String(50), nullable=False)
    model = tables.Column(tables.String(50), nullable=False)
    year = tables.Column(tables.Integer, nullable=False)
    color = tables.Column(tables.String(50), nullable=False)

    def __init__(self, make, model, year, color):
        self.make = make
        self.model = model
        self.year = year
        self.color = color

    def __repr__(self):
        return f"<Dream car {self.id}: {self.make} {self.model} ({self.year}) - {self.color}>\n"
    
    def to_dict(self):
        return {
            'id': self.id,
            'make': self.make,
            'model': self.model,
            'year': self.year,
            'color': self.color
        }

with app.app_context():
    
    tables.create_all()