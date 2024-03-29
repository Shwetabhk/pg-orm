"""
Query Utils Class
"""
from typing import Dict


class Query:
    """
    Query class to make condtional queries
    """
    def __init__(self, **conditions: Dict[str, any]):
        """
        Query Data Class constructor
        :param field_name: name of the field
        :param operator: comparison operator
        :param value: comparison value
        """
        self.conditions = conditions

    def __get_sql_format(self):
        """
        Compute where clause token
        :return: where clause token string
        """
        where_clause = ''
        condition_counter = 1
        for condition in self.conditions:

            # Null Check case handling
            if self.conditions[condition]['operator'] == '=' and self.conditions[condition]['value'] is None:
                self.conditions[condition]['operator'] = 'IS'
                self.conditions[condition]['value'] = 'NULL'

                where_clause = "{0} {1} {2} {3}".format(
                    where_clause, 
                    condition, 
                    self.conditions[condition]['operator'], self.conditions[condition]['value']
                )

            else: 
                where_clause = "{0} {1} {2} '{3}'".format(
                    where_clause,
                    condition,
                    self.conditions[condition]['operator'], self.conditions[condition]['value']
                )

            if condition_counter != len(self.conditions.keys()):
                where_clause = '{0} AND'.format(where_clause)
            condition_counter = condition_counter + 1
        return where_clause

    def __str__(self):
        """
        String representation of class
        :return: sql format of conditions
        """
        return self.__get_sql_format()

    def __or__(self, other):
        """
        Executed with the or operator
        :param other: other instance of class Query
        :return: merged string
        """
        return '{0} OR {1}'.format(self.__get_sql_format(), other.__get_sql_format())

    def __and__(self, other):
        """
        Executed with the and operator
        :param other: other instance of class Query
        :return: merged string
        """
        return '{0} AND {1}'.format(self.__get_sql_format(), other.__get_sql_format())
