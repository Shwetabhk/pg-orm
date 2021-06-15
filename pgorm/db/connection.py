"""
Database connection utils
"""
import os
import psycopg2


class Database:
    """
    Create DataBase Connection
    """
    def __init__(self):
        """
        Initialize Database conection
        """
        self.__db_settings = {
            'host': os.environ.get('DATABASE_HOST'),
            'port': os.environ.get('DATABASE_PORT'),
            'database': os.environ.get('DATABASE_NAME'),
            'user': os.environ.get('DATABASE_USER'),
            'password': os.environ.get('DATABASE_PASSWORD')
        }

        # Triaging connection on initialization
        self.__triage_connection()

    def __triage_connection(self):
        """
        Validate Postgres Credentials
        """
        connection = psycopg2.connect(**self.__db_settings)
        connection.close()

    @property
    def connection(self):
        return psycopg2.connect(**self.__db_settings)
