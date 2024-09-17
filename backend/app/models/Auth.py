from app.extensions import db

class Role(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), unique=True)
    
    def __repr__(self):
        return f'<Role {self.name}>'


class UserAcc(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(150), unique=True, nullable=False)
    password = db.Column(db.String(150), nullable=False)
    prefix = db.Column(db.String(300))
    role_id = db.Column(db.Integer, db.ForeignKey('role.id'), nullable=False)
    role = db.relationship('Role', backref=db.backref('Accounts', lazy=True))
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=True)
    user = db.relationship('User', backref=db.backref('Accounts', lazy=True))
    isActive = db.Column(db.Boolean, default=True)
    
    def __repr__(self):
        return f'<UserAcc {self.username}>'