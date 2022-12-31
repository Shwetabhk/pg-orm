import logging

from .common import (
    run_sql, 
    fetch_db_info
)


logger = logging.getLogger(__name__)


def alter(table_name: str, fields: dict, cursor) -> str:
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

            run_sql(sql=sql, cursor=cursor)
