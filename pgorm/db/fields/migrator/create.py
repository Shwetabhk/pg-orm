import logging

from psycopg2 import errors

from .common import (
    run_sql, 
    fetch_db_info,
    rollback
)


logger = logging.getLogger(__name__)


SQL_CREATE_STATEMENT = "CREATE TABLE {table_name} ({fields});"


def create_or_alter(table_name: str, fields: dict) -> str:
    """
    Create Table Query
    :param table_name: Name of the Table
    :param fields: Fields of the Table
    :return: Create Table Query
    """
    creation_string = ', '.join(
        [
            '{0} {1}'.format(
                field,
                fields[field]
            ) for field in fields
        ]
    )

    sql = SQL_CREATE_STATEMENT.format(table_name=table_name, fields=creation_string)
    
    logger.debug(sql)

    try:
        run_sql(sql=sql)
    except errors.DuplicateTable:
        logger.warning('Table {0} already exists'.format(table_name))
        rollback()
        alter(table_name=table_name, fields=fields)


def alter(table_name: str, fields: dict) -> str:
    """
    Alter Table Query
    :param table_name: Name of the Table
    :param fields: Fields of the Table
    :return: Alter Table Query
    """
    # Get all the fields of the table
    table_fields = fetch_db_info(table_name=table_name)

    # Compare the fields with the received fields
    for field in fields.keys():
        if field not in table_fields:
            # Add the field to the table
            sql = "ALTER TABLE {0} ADD COLUMN {1} {2};".format(table_name, field, fields[field])
            
            logger.debug(sql)

            run_sql(sql=sql)
