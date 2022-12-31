import logging

from psycopg2 import errors

from .common import (
    run_sql, 
    rollback
)


logger = logging.getLogger(__name__)


SQL_CREATE_STATEMENT = "CREATE TABLE {table_name} ({fields});"


def generate_create_statement(table_name: str, fields: dict) -> str:
    """
    Generate Create Table Statement
    :param table_name: Name of the Table
    :param fields: Fields of the Table
    :return: Create Table Statement
    """
    # Generate Create Table Statement
    creation_string = ', '.join(
        [
            '{0} {1}'.format(
                field,
                fields[field]
            ) for field in fields
        ]
    )

    sql = SQL_CREATE_STATEMENT.format(table_name=table_name, fields=creation_string)

    return sql


def create(statement: str, table_name: str, cursor) -> str:
    """
    Create Table Query
    :param table_name: Name of the Table
    :param fields: Fields of the Table
    :return: Create Table Query
    """
    try:
        run_sql(sql=statement, cursor=cursor)
    except errors.DuplicateTable:
        logger.warning('Table {0} already exists'.format(table_name))
        rollback()
