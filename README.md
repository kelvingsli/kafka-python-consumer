## Kafka Python Consumer
---
### Summary

Application will consume Kafka events and parse into python objects using Protobuf deserializers. Consumer will push events into an internal mulitprocessing queue. A separate process will retrieve the event items and upsert into a database. The Kafka consumer is start in a separate thread and the database upsert is handled in a separate process.

---

### Setup

Use the latest version of Python and pip.

Run the following commands to setup the virtual environment for the project

```
python -m venv .venv
source .venv/Scripts/activate
```
Install all the necessary packages after the virtual environment is setup.

```
pip install -r requirement.txt
```

---

### Configuration

Use the `.sample-env` and update it with the necessary credentials. Save the file with the filename `.env`. If deploying using Docker, update `.sample-docker-env`. Save the file with the filename `.docker-env`.

`DB_URL` is the database url to connect. Add port number.
`DB_USER` is the database user.
`DB_PASSWORD` is the database password.
`DB_DATABASE` is the default database to connect to.
`KAFKA_BROKER_URL` is the Kafka broker connection. Add port number.
`KAFKA_SCHEMA_REGISTRY_URL` is the Kafka schema registry link. Add port number.
`LOGPATH` is the internal log directory path.

---

### Running application

Run the command. Note to use a different port for the Kafka producer service if the services are run on the same machine.
```
flask run -p 5001
```