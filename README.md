# 🚀 Task Manager API

## 📋 Sobre o Projeto
Uma **API RESTful** desenvolvida em **Python** com **Flask** para gerenciamento de tarefas. O projeto utiliza um banco de dados relacional **SQL** para persistência dos dados, simulando um ambiente de back-end real.

Este projeto demonstra:
* Desenvolvimento de rotas e endpoints (GET, POST, PUT, DELETE).
* Manipulação de Banco de Dados com ORM (SQLAlchemy).
* Estruturação de respostas em JSON.

## 🛠 Tecnologias
* **Python 3**
* **Flask** (Microframework Web)
* **SQLAlchemy** (ORM para Banco de Dados)
* **SQLite** (Banco de dados SQL em arquivo)

## 🔌 Endpoints da API

| Método | Rota | Descrição |
| :--- | :--- | :--- |
| `POST` | `/tasks` | Cria uma nova tarefa |
| `GET` | `/tasks` | Lista todas as tarefas |
| `PUT` | `/tasks/<id>` | Atualiza o status de uma tarefa |
| `DELETE` | `/tasks/<id>` | Remove uma tarefa |

## ⚙️ Como rodar

```bash
# Instale as dependências
pip install -r requirements.txt

# Execute a aplicação
python app.py
