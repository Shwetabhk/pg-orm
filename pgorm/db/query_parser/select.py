"""
SELECT Query Parser
"""
from typing import List

from pgorm.db.conditions import Query

SELECT_QUERY = "SELECT {field_names} FROM {table_name} {where_clause} {limit_offset};"


def get_parsed_select_query(
        table_name: str, field_names: List[str] = None,
        where_clause: Query = None, offset: int = None, limit: int = None
):
    """
    Parse get query according to the received params
    :param table_name: name of the table to fetch from
    :param field_names: attributes to be selected
    :param where_clause: where clause generated by query class
    :param limit: limit number of records
    :param offset: offset of the page
    :return: Parsed select query
    """
    # Parsing Select Field Names
    field_names_token = ''
    if not field_names:
        field_names_token = '*'
    else:
        for field_name in field_names:
            field_names_token = '{}, {}'.format(field_names_token, field_name)
        field_names_token = field_names_token[2:]

    if where_clause:
        where_clause = 'WHERE {0}'.format(where_clause)

    # Define limit and offset in the query
    limit_offset_token = ''

    if limit:
        offset = offset if offset else 0
        limit_offset_token = 'LIMIT {0} OFFSET {1}'.format(limit, offset)

    return SELECT_QUERY.format(
        field_names=field_names_token, table_name=table_name,
        where_clause=where_clause, limit_offset=limit_offset_token
    )
