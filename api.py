import os
import sys
from flask import Flask
from flask_restful import Api
from flask_cors import CORS

from employees.models import Employees
from employees.views import EmployeesAPI

os.environ.setdefault('DATABASE_HOST', 'localhost')
os.environ.setdefault('DATABASE_PORT', '5432')
os.environ.setdefault('DATABASE_NAME', 'pgorm')
os.environ.setdefault('DATABASE_USER', 'postgres')
os.environ.setdefault('DATABASE_PASSWORD', 'postgres')


app = Flask(__name__)
api = Api(app)

CORS(app)

api.add_resource(EmployeesAPI, '/employees')

if __name__ == '__main__':
    if len(sys.argv) > 1:
        if sys.argv[1] == 'runserver':
            app.run(debug=True)
        elif sys.argv[1] == 'migrate':
            # Migrate models.py of each directory
            from employees.migrations import *
