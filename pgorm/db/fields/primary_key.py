"""
Primary Key Fields are used to define the Primary Key of the Table
"""
class PrimaryKey():
    """
    Class for Serial id Primary key
    """
    def __init__(self, auto_increment: bool = True):
        self.auto_increment = auto_increment

    def __str__(self):
        return 'SERIAL PRIMARY KEY' if self.auto_increment else 'SERIAL'
    
    def __repr__(self):
        return 'SERIAL PRIMARY KEY' if self.auto_increment else 'PRIMARY KEY'

    def __eq__(self, other):
        return self.__dict__ == other.__dict__
