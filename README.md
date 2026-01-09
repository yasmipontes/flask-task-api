# 🚀 Task Manager API

![Python](https://img.shields.io/badge/Python-3.10%2B-blue)
![Flask](https://img.shields.io/badge/Flask-2.0%2B-black)
![Status](https://img.shields.io/badge/Status-Completed-success)

## 📖 Sobre o Projeto

O **Task Manager API** é um microsserviço desenvolvido para gerenciar o ciclo de vida de tarefas (To-Do List). 

O objetivo principal deste projeto foi construir uma **API RESTful** robusta, seguindo as melhores práticas de desenvolvimento Back-end, como a separação de responsabilidades, uso de ORM para segurança de dados e padronização de respostas em JSON.

Este projeto simula o back-end de uma aplicação real, pronta para ser consumida por qualquer Front-end (Web ou Mobile).

---

## ⚙️ Arquitetura e Decisões Técnicas

Durante o desenvolvimento, tomei decisões focadas em **escalabilidade** e **manutenibilidade**:

* **Microframework Flask:** Escolhido por ser leve e permitir controle total sobre a construção das rotas e requisições HTTP.
* **SQLAlchemy (ORM):** Utilizado para abstrair a camada de banco de dados. Ao manipular objetos Python em vez de SQL puro, aumentamos a segurança contra *SQL Injection* e facilitamos a manutenção do código.
* **Design Pattern:** O código foi estruturado separando o **Modelo de Dados** (Representação da Tabela) das **Rotas** (Controllers), mantendo o código organizado.

---

## 🛠 Tech Stack

* **Linguagem:** Python 3
* **Framework Web:** Flask
* **Database:** SQLite (Simplicidade local) / Abstraído via SQLAlchemy
* **Testes de API:** Postman / Insomnia

---

## 🔌 Documentação da API

A API segue os padrões REST, utilizando verbos HTTP para cada ação semântica.

### 📝 Endpoints

| Método | Endpoint | Descrição | Corpo da Requisição (JSON) |
| :--- | :--- | :--- | :--- |
| **POST** | `/tasks` | Cria uma tarefa | `{"title": "Estudar Python"}` |
| **GET** | `/tasks` | Lista tarefas | *Nenhum* |
| **PUT** | `/tasks/<id>` | Atualiza status | *Nenhum* (Alterna T/F) |
| **DELETE**| `/tasks/<id>` | Remove tarefa | *Nenhum* |

### 🔍 Exemplo de Resposta (JSON)

```json
[
  {
    "id": 1,
    "title": "Finalizar desafio técnico",
    "done": false
  },
  {
    "id": 2,
    "title": "Estudar Flask",
    "done": true
  }
]
