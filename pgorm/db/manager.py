"""
Base manager class to do SQL operations over DB rows
"""
from typing import List, Dict

from .connection import Database
from .query_parser import select


class BaseManager:
    """
    Base Manager which will perform all the SQL operations
    """
    def __init__(self, model_class):
        self.model_class = model_class
        self.connection = None

    def select(self, field_names: List[str] = None, conditions: Dict = None, offset: int = None, limit: int = None):
        """
        Run a select query based on params
        :param field_names: Name of the fields to be selected
        :param conditions: Where clause conditions
        :param offset: Offset of records to fetch
        :param limit: Limit of records to fetch
        :return:
        """
        # Instantiate Databse
        instance: Database = Database()
        db_cursor = instance.cursor

        # Construct Query
        table_name = self.model_class.table_name
        query = select.get_parsed_select_query(
            table_name=table_name, field_names=list(field_names),
            params=conditions, offset=offset, limit=limit
        )

        # Execute query and return results
        print('Execting: ', query)
        db_cursor.execute(query)
        return db_cursor.fetchall()

    def bulk_insert(self, rows: list):
        pass

    def update(self, new_data: dict):
        pass

    def delete(self):
        pass


class MetaModel(type):
    """
    Model Metadata class with properties
    """
    manager = BaseManager

    def __get_manager(self):
        return self.manager(model_class=self)

    @property
    def objects(self):
        return self.__get_manager()
