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

    employees = Employees.objects.select(
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

    employees = [dict(employee) for employee in employees]
    print(employees)
