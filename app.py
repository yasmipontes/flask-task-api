from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
import os

# Configuração da Aplicação
app = Flask(__name__)

# Configuração do Banco de Dados (SQLite para simplicidade local)
basedir = os.path.abspath(os.path.dirname(__file__))
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'tasks.db')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Inicializando o Banco
db = SQLAlchemy(app)

# --- MODELO (BANCO DE DADOS) ---
class Task(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    done = db.Column(db.Boolean, default=False)

    def to_json(self):
        return {
            "id": self.id,
            "title": self.title,
            "done": self.done
        }

# Cria as tabelas no banco automaticamente ao iniciar
with app.app_context():
    db.create_all()

# --- ROTAS (API) ---

@app.route('/tasks', methods=['POST'])
def add_task():
    """Cria uma nova tarefa no banco de dados"""
    title = request.json['title']
    new_task = Task(title=title)
    
    db.session.add(new_task)
    db.session.commit()
    
    return jsonify(new_task.to_json()), 201

@app.route('/tasks', methods=['GET'])
def get_tasks():
    """Busca todas as tarefas salvas"""
    tasks = Task.query.all()
    # List Comprehension para formatar os dados
    return jsonify([task.to_json() for task in tasks])

@app.route('/tasks/<int:id>', methods=['PUT'])
def update_task(id):
    """Atualiza o status de uma tarefa (Feito/Não feito)"""
    task = Task.query.get_or_404(id)
    task.done = not task.done # Inverte o status
    
    db.session.commit()
    return jsonify(task.to_json())

@app.route('/tasks/<int:id>', methods=['DELETE'])
def delete_task(id):
    """Deleta uma tarefa"""
    task = Task.query.get_or_404(id)
    
    db.session.delete(task)
    db.session.commit()
    return jsonify({"message": "Tarefa deletada com sucesso!"})

if __name__ == '__main__':
    app.run(debug=True)