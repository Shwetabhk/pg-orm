"""
INSERT Query parser
"""
from typing import Dict

SINGLE_INSERT_QUERY = "INSERT INTO {table_name} ({column_names}) VALUES ({values}) RETURNING id, {column_names};"


def get_parsed_single_insert_query(table_name: str, record: Dict):
    """
    Parse insert query according to the received record
    :param table_name: name of the table to fetch from
    :param record: Record to be created
    :return: Parsed insert query
    """
    column_names = ''
    values = ''

    for field in record:
        column_names = '{0}, {1}'.format(column_names, field)
        values = "{0}, '{1}' ".format(values, record[field])

    column_names = column_names[2:]
    values = values[2:]

    return SINGLE_INSERT_QUERY.format(table_name=table_name, column_names=column_names, values=values)
