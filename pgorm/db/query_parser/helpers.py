"""
Query parser helper functions
"""
from typing import Dict


def compute_where_clause(params: Dict):
    """
    Compute where clause token
    :param params: Where clause parameters
    :return: where clause token string
    """
    where_clause = 'where '
    param_counter = 1
    for param in params:
        where_clause = "{0} {1} {2} '{3}'".format(
            where_clause, param, params[param]['operator'], params[param]['value'])
        if param_counter != len(params.keys()):
            where_clause = '{0} and'.format(where_clause)
        param_counter = param_counter + 1

    return where_clause
