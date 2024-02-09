from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Student(db.Model):
    __tablename__ = 'students'

    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String, unique = True)
    created_at = db.Column(db.DateTime, server_default = db.func.now())
    updated_at = db.Column(db.DateTime, onupdate = db.func.now())

    homeroom_id = db.Column(db.Integer, db.ForeignKey('classes.id'))

    def __repr__(self):
        return f"Name: {self.name}"

class Class(db.Model):
    __tablename__ = 'classes'

    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String)
    teacher_name = db.Column(db.String)
    created_at = db.Column(db.DateTime, server_default = db.func.now())
    updated_at = db.Column(db.DateTime, onupdate = db.func.now())

    def __repr__(self):
        return f"Name: {self.name}; Teacher Name: {self.teacher_name}"