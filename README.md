# Uncommon Store

This is the Uncommon Store web application, built with Django. The application allows users to browse, add to a cart, and purchase unique fashion items.

## Getting Started

To get this project up and running locally on your machine, follow the instructions below.

### Prerequisites

- Python 3.x
- Django
- Docker (optional if using Docker to run the app)

### Virtual Environment Setup (venv)

1. Clone the repository:
    ```bash
    git clone https://github.com/your-username/uncommonstore.git
    cd uncommonstore
    ```

2. Create a virtual environment:
    ```bash
    python3 -m venv venv
    ```

3. Activate the virtual environment:
    - On macOS/Linux:
      ```bash
      source venv/bin/activate
      ```
    - On Windows:
      ```bash
      venv\Scripts\activate
      ```

4. Install the required dependencies:
    ```bash
    pip install -r requirements.txt
    ```

5. Set up the environment variables:
    - Create a `.env` file in the `ecom/` directory (next to `settings.py`) with the following:
      ```
      SECRET_KEY=<Your_Secret_Key>
      DEBUG=True
      ```
    > Note: You must add your own `SECRET_KEY`. You can generate one using Django's key generation function:
    ```bash
    python -c "from django.core.management.utils import get_random_secret_key; print(get_random_secret_key())"
    ```

6. Apply the database migrations:
    ```bash
    python manage.py migrate
    ```

7. Run the development server:
    ```bash
    python manage.py runserver
    ```

You should now be able to view the site at `http://127.0.0.1:8000`.

### Running with Docker

1. Ensure Docker is installed and running on your system.
2. Build the Docker image:
    ```bash
    docker build -t uncommonstore-app .
    ```

3. Run the Docker container:
    ```bash
    docker run -p 8000:8000 uncommonstore-app
    ```

4. View the app at `http://127.0.0.1:8000`.

### Security Note

Ensure you do **not** commit sensitive data (such as secret keys, passwords, or tokens) to version control. Use environment variables and `.gitignore` to exclude these from the repository.

### .gitignore File

Ensure your `.gitignore` includes the following to avoid tracking sensitive or unnecessary files:

*.pyc 
*.pyo 
pycache/ 
*.env venv/ virtualenv/ 
*.sqlite3 
.DS_Store