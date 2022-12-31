from pgorm.db.connection import Database


def __get_cursor_and_connection():
    """
    Private function to return cursor and connection
    """
    instance: Database = Database()
    connection = instance.connection
    db_cursor = connection.cursor()

    return db_cursor, connection


def run_sql(sql: str, cursor) -> None:
    """
    Run SQL Query
    :param sql: SQL Query
    :return: None
    """
    # Execute query and return results

    cursor.execute(sql)


def fetch_db_info(table_name: str) -> list:
    """
    Get all the fields of the table
    :param table_name: Name of the Table
    :param database: Database Instance
    :return: List of Fields
    """
    # Execute query and return results
    db_cursor, _ = __get_cursor_and_connection()

    db_cursor.execute(
        "SELECT column_name FROM information_schema.columns WHERE table_name='{0}'".format(table_name)
    )
    return [record[0] for record in db_cursor.fetchall()]


def rollback():
    """
    Rollback DB Transaction
    """
    cursor, _ = __get_cursor_and_connection()

    cursor.execute("ROLLBACK")
