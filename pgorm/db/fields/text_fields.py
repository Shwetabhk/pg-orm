"""
All text fields are defined here
"""


class VarChar():
    """
    Instantiate a VarChar Field
    """
    def __init__(self, max_length: int, default: str = None, null: bool = False):
        """
        Instantiate a VarChar Field
        :param max_length: Maximum length of the field
        :param default: Default value of the field
        :param null: If the field can be null
        """
        self.max_length = max_length
        self.default = default
        self.null = null
        self.max_length = max_length
    
    def __str__(self):
        return "VARCHAR({})".format(self.max_length)
    
    def __repr__(self):
        return "VARCHAR({})".format(self.max_length)
    
    def __eq__(self, other):
        return self.__dict__ == other.__dict__


class Text():
    """
    Instantiate a Text Field
    """
    def __init__(self, default: str = None, null: bool = False):
        """
        Instantiate a Text Field
        :param default: Default value of the field
        :param null: If the field can be null
        """
        self.default = default
        self.null = null
    
    def __str__(self):
        return "TEXT"
    
    def __repr__(self):
        return "TEXT"
    
    def __eq__(self, other):
        return self.__dict__ == other.__dict__
