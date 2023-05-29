## Data Engineering Assignment

This repository contains a solution for a data engineering assignment that involves extracting employee data from a CSV file and loading it into a MongoDB database.

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





## Objective

In this assignment, you will build an [Extract, Transform, and Load (ETL)](https://en.wikipedia.org/wiki/Extract,_transform,_load) pipeline with a focus on [Test-Driven Development (TDD)](https://en.wikipedia.org/wiki/Test-driven_development) by performing the following tasks:

1. Read data from a CSV file (`employee_details.csv`)
2. Transform the data
3. Load the data into a MongoDB database
4. Implement the ETL pipeline using Docker Compose

## Requirements

- [Python 3.8+](https://www.python.org/)
- [Docker Compose](https://docs.docker.com/compose/)
- [MongoDB](https://www.mongodb.com/)
- Any other libraries or tools are allowed as long as they are open-source and free to use

## Instructions

### 1. Reading Data from CSV

Create a `read_csv()` method that takes a file path as an argument and reads the CSV file. Return an in-memory data structure such as a list of dictionaries or a Pandas DataFrame.

### 2. Transforming the Data

Create a `transform_data()` method that takes the in-memory data structure from the previous step as an argument.
Perform the following transformation tasks:

1. Convert the `BirthDate` from the format `YYYY-MM-DD` to `DD/MM/YYYY`.
2. Do some cleaning on `FirstName` and `LastName` columns when needed and remove any leading/trailing spaces.
3. Merge the `FirstName` and `LastName` columns into a new column named `FullName`.
4. Calculate each employee's age from the `BirthDate` column using as reference **Jan 1st, 2023**. Add a new column named `Age` to store the computed age.
5. Add a new column named `SalaryBucket` to categorize the employees based on their salary as follows:
  - `A` for employees earning below `50.000`
  - `B` for employees earning between `50.000` and `100.000`
  - `C` for employees earning above `100.000`
6. Drop columns `FirstName`, `LastName`, and `BirthDate`.

### 3. Loading the Data into MongoDB

Create a `load_data()` method that takes the transformed data as an argument, connects to the MongoDB database and inserts the given data into a predefined collection. Ensure that your function creates indexes, if required, to improve performance.

### 4. Docker Compose

Create a `Dockerfile` to create a Docker image of your Python application.

Set up a `docker-compose.yml` file where you will define the services and configure the details such as containers, networks, and volumes for your application.
Configure two services: a Python application with your ETL pipeline and a MongoDB database. Ensure that both services can communicate with each other.

## Deliverables

The *minimum* we expect to see in your submission is:

- `main.py`, the main ETL script containing the core methods: `read_csv()`, `transform_data()`, and `load_data()`.
- Test suites for everthing you think should be tested.
- A `Dockerfile` to create a Docker image of the Python application.
- A `docker-compose.yml` file defining the required services.
- A `README.md` file with instructions for setting up and running the ETL pipeline using Docker Compose.

Upon the completion of the assignment, you should have an ETL pipeline that reads data from a CSV file (`employee_details.csv`), performs the required transformations, and loads the transformed data into a MongoDB database, using Docker Compose and with a focus on Test-Driven Development.

## Submission

Please submit your assignment as a link to a GitHub repository containing the required files. You can also create a private repository and share it with us.

## Notes

- We will value your focus on TDD throughout all the development process.
- If you're familiar with an ETL framework such as [Apache Airflow](https://airflow.apache.org/) or [Luigi](https://github.com/spotify/luigi), feel free to use them to implement the ETL pipeline and document your approach accordingly in the `README.md` file.
