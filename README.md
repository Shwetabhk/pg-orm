# pgorm

Python based ORM for Postgres CRUD Operations

## Description

ORM for easily connecting to Postgres DB and make CRUD operations on tables relatively easy and more flexible without writing any SQL.
This project is under development and method contracts and structure might change rapidly, please reach out to shwetabh002@gmail.com if you wish to contribute.

## Features

* Single Insert
* Select with or without pagination
* Update based on conditions
* Update based on id
* Delete based on conditions
* Update based on id

## Features Under Development

* Support `in` clause in Select Queries - https://github.com/Shwetabhk/pg-orm/issues/3
* Bulk Insert of Records - https://github.com/Shwetabhk/pg-orm/issues/1
* Bulk Update of Records - https://github.com/Shwetabhk/pg-orm/issues/2

## How to Install

* Clone the repository from Github
* Run the following command to install requirements -
  ```bash
  pip install requirements.txt
  ```
* The module will soon be available through PyPi.

## How to Use

### Instantiate the Model class and set DB credentials as environment variables for ORM to pick them up

```python
import os
from pgorm.db.models import Model

os.environ.setdefault('DATABASE_HOST', 'localhost')
os.environ.setdefault('DATABASE_PORT', '5433')
os.environ.setdefault('DATABASE_NAME', 'pgorm')
os.environ.setdefault('DATABASE_USER', 'postgres')
os.environ.setdefault('DATABASE_PASSWORD', 'postgres')

class Employees(Model):
    table_name = 'employees'
```

### Single Insert

```python
from pgorm.db.models import Model


class Employees(Model):
    table_name = 'employees'
    

employeee_to_be_created = {
    'first_name': 'Shwetabh',
    'last_name': 'Kumar',
    'salary': '10000',
    'grade': 'L3'
}

employee_created = Employees.records.insert(**employeee_to_be_created)
```

### Select

```python
from pgorm.db.models import Model
from pgorm.db.conditions import Query


class Employees(Model):
    table_name = 'employees'
    
employees = Employees.records.select(
    field_names=['id', 'first_name', 'last_name', 'salary', 'grade'],
    conditions=Query(
        first_name={
            'operator': '=', 'value': 'Renaud'
        }, id={
            'operator': '=', 'value': 1
        }
    ) | Query(
        first_name={
            'operator': '=', 'value': 'Renaud'
        }, id={
            'operator': '=', 'value': 1
        }
    ),
    limit=1,
    offset=0
)
```

### Update By Condition

```python
from pgorm.db.models import Model
from pgorm.db.conditions import Query


class Employees(Model):
    table_name = 'employees'

values = {
    'first_name': 'Shwetabh',
    'last_name': 'Kumar',
    'salary': '10000',
    'grade': 'L3'
}

Employees.records.update(conditions=Query(first_name={
    'operator': '=', 'value': 'Shwetabh'
}), values=values)
```

### Update By Id

```python
from pgorm.db.models import Model

class Employees(Model):
    table_name = 'employees'

employee_to_be_updated = {
    'first_name': 'Shwetabh',
    'last_name': 'Kumar',
    'salary': '10000',
    'grade': 'L3'
}

updated_employee = Employees.records.update_by_id(id=1, record=employee_to_be_updated)
```

### Delete By Condition

```python
from pgorm.db.models import Model
from pgorm.db.conditions import Query


class Employees(Model):
    table_name = 'employees'


Employees.records.delete(Query(id={
    'operator': '=', 'value': 1
}))
```

### Delete By Id

```python
from pgorm.db.models import Model

class Employees(Model):
    table_name = 'employees'

employee_to_be_updated = {
    'first_name': 'Shwetabh',
    'last_name': 'Kumar',
    'salary': '10000',
    'grade': 'L3'
}

Employees.records.delete_by_id(id=1)
```

## Contributions

The repository is not actively accepting contributions. Please reach out to shwetabh002@gmail.com for any help or create and issue on github.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details
