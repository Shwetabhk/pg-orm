from pgorm.db.manager import MetaModel

from pgorm.db.fields.migrator import create_or_alter


class Model(metaclass=MetaModel):
    """
    Model Class to be Inherited by all Models.
    """
    table_name = ''

    def create_migration(self):
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

        # Construct Query
        table_name = self.table_name
        create_or_alter(
            table_name=table_name, fields=fields
        )
