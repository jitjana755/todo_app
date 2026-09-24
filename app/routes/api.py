from flask import Blueprint, request, jsonify
from app import db
from app.models import Task

api_bp = Blueprint('api', __name__, url_prefix='/api')


# =========================
# GET ALL TASKS
# =========================
@api_bp.route('/tasks', methods=['GET'])
def get_tasks():
    tasks = Task.query.all()

    return jsonify([
        {
            'id': task.id,
            'title': task.title,
            'status': task.status
        }
        for task in tasks
    ])


# =========================
# GET SINGLE TASK
# =========================
@api_bp.route('/tasks/<int:task_id>', methods=['GET'])
def get_task(task_id):
    task = Task.query.get_or_404(task_id)

    return jsonify({
        'id': task.id,
        'title': task.title,
        'status': task.status
    })


# =========================
# CREATE NEW TASK
# =========================
@api_bp.route('/tasks', methods=['POST'])
def create_task():
    data = request.get_json()

    if not data or 'title' not in data:
        return jsonify({
            'error': 'Title is required'
        }), 400

    task = Task(
        title=data['title'],
        status=data.get('status', 'pending')
    )

    db.session.add(task)
    db.session.commit()

    return jsonify({
        'message': 'Task created successfully',
        'id': task.id,
        'title': task.title,
        'status': task.status
    }), 201


# =========================
# UPDATE TASK
# =========================
@api_bp.route('/tasks/<int:task_id>', methods=['PUT'])
def update_task(task_id):
    task = Task.query.get_or_404(task_id)

    data = request.get_json()

    if 'title' in data:
        task.title = data['title']

    if 'status' in data:
        task.status = data['status']

    db.session.commit()

    return jsonify({
        'message': 'Task updated successfully',
        'id': task.id,
        'title': task.title,
        'status': task.status
    })


# =========================
# DELETE TASK
# =========================
@api_bp.route('/tasks/<int:task_id>', methods=['DELETE'])
def delete_task(task_id):
    task = Task.query.get_or_404(task_id)

    db.session.delete(task)
    db.session.commit()

    return jsonify({
        'message': 'Task deleted successfully'
    })
{
    "message": "Task updated successfully",
    "id": 1,
    "title": "Updated Bangali",
    "status": "working"
}