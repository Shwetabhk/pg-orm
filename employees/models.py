from typing import Dict

from pgorm.db import models, fields


class Employees(models.Model):
    table_name = 'employees'

    id = fields.PrimaryKey(auto_increment=True)
    email = fields.VarChar(max_length=255, default=None, null=True)
    first_name = fields.VarChar(max_length=255, default=None, null=True)
    last_name = fields.VarChar(max_length=255, default=None, null=True)
    salary = fields.VarChar(max_length=255, default=None, null=True)
    grade = fields.VarChar(max_length=255, default=None, null=True)

    def create(employee: Dict):
        return Employees.records.insert(**employee)
    
    def get_all():
        return Employees.records.select()
    
    def get_by_id(id: int):
        return Employees.records.select(conditions={'id': id})
    
    def update_by_id(id: int, employee: Dict):
        return Employees.records.update_by_id(id=id, record=employee)
    
    def delete_by_id(id: int):
        return Employees.records.delete_by_id(id=id)
    
    def delete_all():
        return Employees.records.delete()
