"""
DELETE Query parser
"""
from typing import Dict

DELETE_QUERY = "DELETE FROM {table_name} {where_clause};"


def get_parsed_delete_query(table_name: str, where_clause: Dict = None):
    """
    Parse delete query according to the received record
    :param table_name: Name of the table
    :param where_clause: Where Clause String
    :return: Parsed Delete Query
    """
    if where_clause:
        where_clause = 'WHERE {0}'.format(where_clause)

    return DELETE_QUERY.format(table_name=table_name, where_clause=where_clause)
