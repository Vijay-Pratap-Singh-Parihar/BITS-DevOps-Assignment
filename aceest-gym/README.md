# Aceest Gym API

Minimal Flask backend for gym/fitness member management (in-memory storage).

## Setup

1. Create and activate a virtual environment (recommended):

   ```bash
   python -m venv venv
   ```

   On Windows:

   ```bash
   venv\Scripts\activate
   ```

   On macOS/Linux:

   ```bash
   source venv/bin/activate
   ```

2. Install dependencies:

   ```bash
   pip install -r requirements.txt
   ```

## Run

From the project root (`aceest-gym/`):

```bash
python app/app.py
```

The server listens on `http://127.0.0.1:5000` by default.

## API overview

| Method | Path       | Description        |
| ------ | ---------- | ------------------ |
| GET    | `/health`  | Health check       |
| GET    | `/members` | List members       |
| POST   | `/members` | Add a member (JSON)|

## CI/CD Pipeline

### GitHub Actions

- Triggered on every push and pull request
- Installs dependencies
- Runs pytest test suite
- Builds Docker image

### Jenkins

- Pulls latest code from repository
- Installs dependencies
- Runs test suite
- Builds Docker image
- Acts as secondary validation layer

## Running Tests

From the project root (`aceest-gym/`):

```bash
pytest -v
```

## Docker Usage

From the project root (`aceest-gym/`):

Build image:

```bash
docker build -t aceest-gym-app .
```

Run container:

```bash
docker run -p 5000:5000 aceest-gym-app
```
