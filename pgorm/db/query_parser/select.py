from typing import List, Dict
from .helpers import compute_where_clause

SELECT_QUERY = "select {field_names} from {table_name} {where_clause} {limit_offset};"


def get_parsed_select_query(
        table_name: str, field_names: List[str] = None,
        params: Dict = None, offset: int = None, limit: int = None
):
    """
    Parse get query according to the received params
    :param table_name: name of the table to fetch from
    :param field_names: attributes to be selected
    :param params: where clause params
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

    # Parse Params
    where_clause = ''
    if params:
        where_clause = compute_where_clause(params)

    # Define limit and offset in the query
    limit_offset_token = ''

    if limit:
        offset = offset if offset else 0
        limit_offset_token = 'limit {0} offset {1}'.format(limit, offset)

    return SELECT_QUERY.format(
        field_names=field_names_token, table_name=table_name,
        where_clause=where_clause, limit_offset=limit_offset_token
    )
