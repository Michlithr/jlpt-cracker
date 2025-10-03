Readme
# JLPT Cracker Backend

A FastAPI application for a JLPT study tool.

This repository contains the backend for the JLPT Cracker application. It uses FastAPI for the API, SQLModel for the ORM, and PostgreSQL as the database. The entire development environment is containerized using Docker Compose.

## 🚀 Getting Started

Follow these steps to set up and run the project on your local machine.

### Prerequisites

-   **Docker Desktop:** This includes Docker Engine and Docker Compose.
-   **Python 3.11:** The project requires Python 3.11 for dependency management with Poetry.
-   **Poetry:** Install the Poetry package manager.

### Local Development Setup

1.  **Clone the repository:**
    ```bash
    git clone git@github.com:Michlithr/jlpt-cracker.git
    cd jlpt-cracker/backend
    ```

2.  **Configure Poetry:** Ensure Poetry is using the correct Python version.
    ```bash
    poetry env use python3.11
    ```

3.  **Install dependencies and generate `poetry.lock`:**
    ```bash
    poetry install
    ```

### Running the Application with Docker

Make sure you are in the project's root directory (`jlpt-cracker/`).

1.  **Build and run the Docker containers:**
    ```bash
    docker compose up --build
    ```
    This command will build the Docker images and start the backend and database services.

2.  **Access the API:**
    -   The FastAPI application will be running at `http://localhost:8000`.
    -   The interactive API documentation (Swagger UI) is available at `http://localhost:8000/docs`.


### Stopping the Application

To stop the containers, press `Ctrl + C` in the terminal where Docker Compose is running, or if it's running in detached mode, use:
```bash
docker compose down