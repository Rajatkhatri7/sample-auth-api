

## Getting Started

To get started, follow these steps:

1. Clone this project:

```
git clone https://github.com/Rajatkhatri7/xpaybacktasks
```

2. Create a virtual environment:

```
python3 -m venv xpaybackenv
```

3. Activate the virtual environment:

```
source xpaybackenv/bin/activate
```

4. Install the dependencies:

```
pip install -r requirements.txt
```

5. Install Postgres and create a database:

* Follow the instructions on the Postgres download page: https://www.postgresql.org/download/ to install Postgres.
* Create a database in Postgres.

6. Create a `.env` file and add the following environment variables:

```
POSTGRES_HOST=localhost
POSTGRES_PORT=5432
POSTGRES_NAME=<your db name here>
POSTGRES_USER=<db user here>
POSTGRES_PASS=<db password here>
```

7. Run the server:

```
uvicorn main:app --host 0.0.0.0 --port 8001 --reload
```

This will start the FastAPI server on port 8001.

## Accessing the API

You can access the API at `http://0.0.0.0:8001`.

## SwaggerUI Documentation

You can access the SwaggerUI documentation at `http://0.0.0.0:8001/docs`. This will allow you to test the APIs directly from the browser.
