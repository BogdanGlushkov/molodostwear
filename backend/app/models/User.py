from app.extensions import db
from datetime import datetime

class Schedule(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    date = db.Column(db.DateTime, nullable=False)
    shift = db.Column(db.String(50), nullable=False)
    type = db.Column(db.String(50), nullable=False)
    breaks = db.Column(db.JSON, nullable=False)  # Используем текстовое поле для хранения JSON
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)

    def __init__(self, date, shift, type, breaks, user_id):
        self.date = date
        self.shift = shift
        self.type = type
        self.breaks = breaks  # Преобразуем список в JSON перед сохранением
        self.user_id = user_id  # Устанавливаем user_id 

    # def get_breaks(self):
    #     return json.loads(self.breaks)  # Преобразуем JSON обратно в список при извлечении
    
    def to_dict(self):
        return {
            'date': str(self.date.isoformat()) + '.000Z',
            'shift': self.shift,
            'type': self.type,
            'breaks': self.breaks
        }

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False, unique=True)
    schedule = db.relationship('Schedule', backref='user', lazy=True)

    def to_dict(self):
        return {
            'id': self.id,
            'name': self.name,
            'schedule': [s.to_dict() for s in self.schedule],
            'projects': [project.to_dict() for project in self.projects]
        }
        
    def to_project(self):
        return {
            'id': self.id,
            'name': self.name, 
        }