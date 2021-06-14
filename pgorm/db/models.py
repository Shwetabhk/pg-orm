from pgorm.db.manager import MetaModel


class Model(metaclass=MetaModel):
    """
    Model Class to be Inherited by all Models.
    """
    table_name = ''
