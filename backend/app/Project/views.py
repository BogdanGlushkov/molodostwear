from flask import Blueprint, request, jsonify
from app.models.Project import Project
from app.models.User import User
from app.extensions import db

project = Blueprint('project', __name__, template_folder='templates')

@project.route('/projects', methods=['POST'])
def create_project():
    data = request.json
    name = data.get('name')
    cost = data.get('cost')
    
    if not name or cost is None:
        return jsonify({'error': 'Invalid data'}), 400

    project = Project(name=name, cost=cost)
    db.session.add(project)
    db.session.commit()

    return jsonify(project.to_dict()), 201

@project.route('/projects', methods=['GET'])
def get_project():
    projects = Project.query.all()
    project_list = [project.to_dict() for project in projects]
    return jsonify(project_list)

@project.route('/projects/<int:project_id>', methods=['PUT'])
def update_project(project_id):
    data = request.json
    project = Project.query.get_or_404(project_id)

    if 'name' in data:
        project.name = data['name']
    if 'cost' in data:
        project.cost = data['cost']
    if 'users' in data:
        # Извлекаем только идентификаторы пользователей
        user_ids = [user['id'] for user in data['users']]
        project.users = User.query.filter(User.id.in_(user_ids)).all()

    db.session.commit()

    return jsonify({
        'id': project.id,
        'name': project.name,
        'cost': project.cost,
        'users': [{'id': user.id, 'name': user.name} for user in project.users]  # Возвращаем полный объект пользователя
    })
    
@project.route('/projects/<int:project_id>', methods=['DELETE'])
def delete_project(project_id):
    project = Project.query.get_or_404(project_id)
    if project is None:
        return jsonify({'error': 'Project not found'}), 404

    db.session.delete(project)
    db.session.commit()

    return jsonify({'message': 'Project deleted successfully'}), 200
