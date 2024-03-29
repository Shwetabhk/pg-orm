import logging

from flask import request
from flask_restful import Resource

from pgorm.db.exceptions import RecordNotFound

from .models import Employees


logger = logging.getLogger(__name__)

class EmployeesAPI(Resource):
    """
    API For Employees
    """

    def post(self):
        data = request.get_json(force=True)
        logger.debug(data)
        return Employees.create(data)

    def get(self):
        return Employees.get_all()

    def put(self):
        data = request.get_json(force=True)
        logger.debug(data)
        try:
            Employees.update_by_id(data['id'], data)
        except RecordNotFound:
            return {
                'error': 'Record not found'
            }, 404

    def delete(self):
        data = request.get_json(force=True)
        logger.debug(data)
        return Employees.delete_by_id(data['id'])
