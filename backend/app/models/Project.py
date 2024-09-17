from app.extensions import db

class Project(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    cost = db.Column(db.Float, nullable=False)
    users = db.relationship('User', secondary='project_user', backref='projects')

    def to_dict(self):
        return {
            'id': self.id,
            'name': self.name,
            'cost': self.cost,
            'users': [user.to_project() for user in self.users]
        }

class ProjectUser(db.Model):
    __tablename__ = 'project_user'
    project_id = db.Column(db.Integer, db.ForeignKey('project.id'), primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), primary_key=True)

    def __init__(self, project_id, user_id):
        self.project_id = project_id
        self.user_id = user_id