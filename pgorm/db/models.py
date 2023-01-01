import logging
import hashlib
from pgorm.db.connection import Database
from pgorm.db.manager import MetaModel

from pgorm.db.fields.migrator import (
    create,
    alter,
    check_or_create_migrations_table,
    get_latest_migration,
    generate_create_statement,
    save_migration
)

from pgorm.db.exceptions import (
    MigrationError
)

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


class Model(metaclass=MetaModel):
    """
    Model Class to be Inherited by all Models.
    """
    table_name = ''

    def register(self):
        """
        Create Migration for the Model
        :return: None
        """
        fields = dict(vars(self.__class__))
        fields.pop('table_name')
        fields.pop('__module__')
        fields.pop('__doc__')

        # Removing all the callable fields
        field_names = list(fields.keys())

        for field in field_names:
            if callable(fields[field]):
                fields.pop(field)

        try:
            # Initialize Database Connection
            connection = Database().connection
            cursor = connection.cursor()

            # Check if migrations table exists else create
            check_or_create_migrations_table(cursor=cursor)

            # get the latest migration for this table

            latest_migration = get_latest_migration(table_name=self.table_name, cursor=cursor)

            statement = generate_create_statement(table_name=self.table_name, fields=fields)

            # convert statement to base64
            hash_code = hashlib.sha256(statement.encode('utf-8')).hexdigest()

            # Check if hash of the latest migration is same as current migration
            if latest_migration and latest_migration['hash_code'] == hash_code:
                return
            
            logger.info('Creating Migration for %s' % self.table_name)
           
            # Increment the version of the migration
            if latest_migration:
                logger.info('Found an existing migration - %s' % latest_migration['name'])
                version = int(latest_migration['name'].split('_')[1]) + 1
            else:
                logger.info('Creating first migration')
                version = 1

            # Generate Migration Name
            migration_name = '{0}_{1}'.format(self.table_name, version)

            save_migration({
                'table_name': self.table_name,
                'name': migration_name,
                'hash_code': hash_code
                },
                cursor=cursor
            )

            # Construct Query
            logger.info('Creating Migration for %s' % self.table_name)

            logger.info('Running Statement: %s' % statement)
            if not latest_migration:
                create(
                    statement=statement,
                    table_name=self.table_name,
                    cursor=cursor
                )
            else:
                alter(
                    table_name=self.table_name,
                    fields=fields,
                    cursor=cursor
                )
            connection.commit()
        except Exception as e:
            # Incase Migration goes wrong, rollback
            logger.error('Migration Failed')
            connection.rollback()
            raise MigrationError(e)
