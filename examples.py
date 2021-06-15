import os
from pgorm.db.models import Model
from pgorm.db.conditions import Query


class Employees(Model):
    table_name = 'employees'


if __name__ == '__main__':
    os.environ.setdefault('DATABASE_HOST', 'localhost')
    os.environ.setdefault('DATABASE_PORT', '5433')
    os.environ.setdefault('DATABASE_NAME', 'pgorm')
    os.environ.setdefault('DATABASE_USER', 'postgres')
    os.environ.setdefault('DATABASE_PASSWORD', 'postgres')

    # Select Query
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

    print(employees)

    # Insert Query
    employeee_to_be_created = {
        'first_name': 'Shwetabh',
        'last_name': 'Kumar',
        'salary': '10000',
        'grade': 'L3'
    }

    employee_created_1 = Employees.records.insert(**employeee_to_be_created)
    print(employee_created_1)

    employee_created_2 = Employees.records.insert(**employeee_to_be_created)
    print(employee_created_2)

    # Delete By Condition
    Employees.records.delete(Query(id={
        'operator': '=', 'value': employee_created_1['id']
    }))

    # Delete By Id
    Employees.records.delete_by_id(id=employee_created_2['id'])

    # Update Query

    employee_to_be_updated = {
        'first_name': 'Shwetabh',
        'last_name': 'Kumar',
        'salary': '100000',
        'grade': 'L4'
    }

    # Update by condition
    employees = Employees.records.update(conditions=Query(first_name={
        'operator': '=', 'value': 'Shwetabh'
    }), values=employee_to_be_updated)

    print(employees)

    # Update by id
    employees = Employees.records.update_by_id(record=employee_to_be_updated, id=1)
    print(employees)
