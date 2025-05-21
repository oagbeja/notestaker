````markdown
# FastAPI Notes Application

This is a FastAPI notes application with user authentication, note management, and async SQLAlchemy.

---

## Features

- User registration and login with JWT authentication
- Create, update, delete, and fetch notes linked to users
- Async database operations with SQLAlchemy
- Enum support for note categories
- Auto-create tables on startup
- Swagger UI with Bearer token authentication

---

## Prerequisites

- Python 3.11 or newer installed
- A database (PostgreSQL, MySQL, SQLite) accessible and configured

---

## Installation

Install dependencies using pip:

```bash
pip install fastapi[standard]
```
````

---

## Configuration

Set your environment variables (e.g., in a `.env` file or your system):

```env
DATABASE_URL=your_database_connection_string
SECRET_KEY=your_jwt_secret_key

```

---

## Running the Application

Start the FastAPI development server with:

```bash
fastapi dev main.py
```

This will start the app with auto-reload enabled.

Then open the Swagger UI at:

```
http://localhost:8000/docs
```

---

## Usage

- Register a user at `/auth/register`
- Login at `/auth/login` to get a JWT token
- Use the **Authorize** button in Swagger UI to provide your Bearer token
- Manage notes at `/notes/` endpoints

---

## Database

- Tables are created automatically on app startup
- Uses async SQLAlchemy ORM
- Relationships between users and notes are enforced via foreign keys

---

## Environment Variables

| Variable       | Description             | Example                                       |
| -------------- | ----------------------- | --------------------------------------------- |
| `DATABASE_URL` | Async DB connection URL | `postgresql+asyncpg://user:pass@localhost/db` |
| `SECRET_KEY`   | JWT signing secret      | `your_secret_key`                             |

---

## Contributing

Feel free to open issues or pull requests.

---

## License

MIT License

---

## Contact

For questions, contact [Joshua Agbeja](mailto:talktogbenga@gmail.com).

```

```
