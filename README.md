## Data Engineering Assignment

This repository contains a solution for a data engineering assignment that involves extracting employee data from a CSV file and loading it into a MongoDB database. Here is the assignement reference: https://github.com/wonderflow-bv/data-engineering-assignment

### Requirements

To run the solution, you need to have the following installed on your machine:

- Docker
- Docker Compose

### Instructions

1. Clone this repository to your local machine.
2. Navigate to the root folder of the repository and run the following command:

```bash
docker compose up
```

This will build and run two containers: one for the Python script that performs the data extraction and loading, and one for the MongoDB database.

3. To verify that the data has been loaded successfully into the database, you can enter the MongoDB container by running the following command:

```bash
docker exec -it data-engineering-assignment-main-mongodb-1 bash
```

4. Inside the container, launch the Mongo shell and run the following commands:

```bash
mongosh
use employees
db.employees.find()
```

This will show you all the documents in the employees collection.