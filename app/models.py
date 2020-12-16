from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Calendar(db.Model):
    __tablename__ = 'calendars'

    id = db.Column(db.Integer, primary_key=True)
    code = db.Column(db.String(10), nullable=False, unique=True)

    events = db.relationship('Event')

    def to_dict(self):
        return {
            'id': self.id,
            'code': self.code,
            'events': [event.to_dict() for event in self.events]
        }

class Event(db.Model):
    __tablename__ = 'events'

    id = db.Column(db.Integer, primary_key=True)
    calendar_id = db.Column(db.Integer, db.ForeignKey('calendars.id'), nullable=False)
    name = db.Column(db.String(25), nullable=False)
    description = db.Column(db.String(500), nullable=True)
    day = db.Column(db.DateTime, nullable=False)
    created_by = db.Column(db.String(25), nullable=True)

    calendar = db.relationship('Calendar')

    def to_dict(self):
        return {
            'id': self.id,
            'calendar_id': self.calendar_id,
            'name': self.name,
            'description': self.description,
            'day': self.day,
            'created_by': self.created_by,
            'calendar': self.calendar.to_dict()
        }