# To-Do App

A small Flask to-do application with a browser-based interface, SQLite storage, and a JSON API.

## Features

- Sign in to view the task page.
- Add tasks and cycle their status between `pending`, `working`, and `done`.
- Create, read, update, and delete tasks through the JSON API.
- Store tasks in a SQLite database.

## Requirements

- Python 3
- pip

## Setup and run

From the repository root, create and activate a virtual environment, install dependencies, and start the app:

### Windows PowerShell

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install -r requirements.txt
python -m app.run
```

### macOS/Linux

```bash
python3 -m venv .venv
source .venv/bin/activate
python -m pip install -r requirements.txt
python -m app.run
```

Open <http://127.0.0.1:5000> in a browser. The SQLite database is created automatically when the app starts.

## Demo login

The current application uses demo credentials:

- Username: `admin`
- Password: `1234`

These credentials and the Flask secret key are hard-coded for demonstration. Do not use them for a public or production deployment; use secure configuration and proper password storage first.

## JSON API

The API is available under `/api`:

| Method | Endpoint | Description |
| --- | --- | --- |
| `GET` | `/api/tasks` | List all tasks |
| `POST` | `/api/tasks` | Create a task (JSON body requires `title`; optional `status`) |
| `GET` | `/api/tasks/<id>` | Get one task |
| `PUT` | `/api/tasks/<id>` | Update a task's `title` and/or `status` |
| `DELETE` | `/api/tasks/<id>` | Delete a task |

Example create request:

```json
{
  "title": "Write project documentation"
}
```

The API currently does not require authentication. Avoid exposing it publicly until access control and input validation are added.
