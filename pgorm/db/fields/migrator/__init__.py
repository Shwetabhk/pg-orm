from pgorm.db.connection import Database
from .create import create, generate_create_statement
from .alter import alter


def check_or_create_migrations_table(cursor):
    """
    Check if 'migrations' table exists
    if not, create it
    if yes, check if migration for this model exists
    if yes, check if migration is same as current model
    if yes, do nothing
    if no, create migration
    """

    cursor.execute(
        "SELECT EXISTS(SELECT * FROM information_schema.tables WHERE table_name='migrations')"
    )
    if not cursor.fetchone()[0]:
        cursor.execute(
            "CREATE TABLE migrations (\
                id SERIAL PRIMARY KEY,\
                table_name VARCHAR(255),\
                name VARCHAR(255),\
                hash_code VARCHAR(255),\
                created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP\
            )"
        )


def get_latest_migration(table_name: str, cursor) -> dict:
    """
    Get the latest migration for the table
    :param table_name: Name of the table
    :return: Latest Migration
    """
    cursor.execute(
        "SELECT * FROM migrations WHERE table_name='{0}' ORDER BY created_at DESC LIMIT 1".format(table_name)
    )
    migration = cursor.fetchone()

    if migration:
        return {
            'id': migration[0],
            'table_name': migration[1],
            'name': migration[2],
            'hash_code': migration[3],
            'created_at': migration[4]
        }


def save_migration(migration: dict, cursor) -> None:
    """
    Save migration to database
    :param migration: Migration
    :return: None
    """
    cursor.execute(
        "INSERT INTO migrations (table_name, name, hash_code) VALUES ('{0}', '{1}', '{2}')".format(
            migration['table_name'],
            migration['name'],
            migration['hash_code']
        )
    )
