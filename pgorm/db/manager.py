"""
Base manager class to do SQL operations over DB rows
"""
from typing import List, Dict

from .conditions import Query
from .connection import Database, RealDictCursor
from .query_parser import select, insert


class BaseManager:
    """
    Base Manager which will perform all the SQL operations
    """
    def __init__(self, model_class):
        self.model_class = model_class
        self.connection = None

    def select(self, field_names: List[str] = None, conditions: Query = None, offset: int = None, limit: int = None):
        """
        Run a select query based on params
        :param field_names: Name of the fields to be selected
        :param conditions: Where clause conditions
        :param offset: Offset of records to fetch
        :param limit: Limit of records to fetch
        :return: Fetched Records
        """
        # Instantiate Database Connection and Cursor
        instance: Database = Database()
        connection = instance.connection
        db_cursor = connection.cursor(cursor_factory=RealDictCursor)

        # Construct Query
        table_name = self.model_class.table_name
        query = select.get_parsed_select_query(
            table_name=table_name, field_names=list(field_names),
            where_clause=conditions, offset=offset, limit=limit
        )

        # Execute query and return results
        db_cursor.execute(query)
        connection.commit()
        return [dict(record) for record in db_cursor.fetchall()]

    def insert(self, **record: Dict):
        """
        Insert Single Record
        :param record: record params or Dictionary
        :return: Created Record
        """
        # Instantiate Database Connection and Cursor
        instance: Database = Database()
        connection = instance.connection
        db_cursor = connection.cursor(cursor_factory=RealDictCursor)

        # Construct Query
        table_name = self.model_class.table_name
        query = insert.get_parsed_single_insert_query(table_name, record)

        # Execute query and return results
        db_cursor.execute(query)
        connection.commit()
        return dict(db_cursor.fetchone())

    def update(self, new_data: Dict):
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
