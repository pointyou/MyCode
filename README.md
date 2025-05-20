# Streamlit Toolbox with API Backend

This project demonstrates a simple separation of front-end and back-end logic. The
core calculations are implemented as plain Python functions under the
`services/` package. A FastAPI application (`backend.py`) exposes these functions
as HTTP endpoints, while the Streamlit application (`frontend.py`) acts purely as
a user interface that calls the backend.

## Prerequisites

- Python 3.11+
- Recommended packages: `fastapi`, `uvicorn`, `requests`, `streamlit`,
  `pydantic`, and `pytest` for running tests.

## Running the Application

1. **Start the backend**:

   ```bash
   uvicorn backend:app --reload
   ```

2. **Start the frontend** in a separate terminal:

   ```bash
   streamlit run frontend.py
   ```

   By default the frontend expects the backend at `http://localhost:8000`.
   Set the environment variable `API_URL` if you run it elsewhere.

## Running Tests

Execute the unit tests with `pytest`:

```bash
pytest
```
