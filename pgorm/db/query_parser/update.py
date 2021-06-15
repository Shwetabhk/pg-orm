"""
UPDATE Query Parser
"""
from typing import Dict

from pgorm.db.conditions import Query

SINGLE_UPDATE_QUERY = "UPDATE {table_name} SET {values} {where_clause} RETURNING id, {column_names};"


def get_parsed_single_update_query(table_name: str, values: Dict, where_clause: Query):
    """
    Parse delete query according to the received record
    :param values: Values to be updated
    :param table_name: Name of the table
    :param where_clause: Where Clause String
    :return: Parsed Delete Query
    """
    column_names = ''
    values_token = ''

    for field in values:
        column_names = '{0}, {1}'.format(column_names, field)
        values_token = "{0}, {1} = '{2}' ".format(values_token, field, values[field])

    column_names = column_names[2:]
    values_token = values_token[2:]

    if where_clause:
        where_clause = 'WHERE {0}'.format(where_clause)

    return SINGLE_UPDATE_QUERY.format(
        table_name=table_name, values=values_token, where_clause=where_clause, column_names=column_names
    )
