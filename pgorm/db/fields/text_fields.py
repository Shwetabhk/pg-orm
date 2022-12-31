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
        # Only default is set
        if self.default:
            return "VARCHAR({}) DEFAULT '{}'".format(self.max_length, self.default)

        # Only null is set
        elif not self.null:
            return "VARCHAR({}) NOT NULL".format(self.max_length)

        # Both default and null are set
        elif self.default and not self.null:
            return "VARCHAR({}) DEFAULT '{}' NOT NULL".format(self.max_length, self.default)

        # No default or null is set
        return "VARCHAR({})".format(self.max_length)
    
    def __repr__(self):
        # Only default is set
        if self.default:
            return "VARCHAR({}) DEFAULT '{}'".format(self.max_length, self.default)
        
        # Only null is set
        elif not self.null:
            return "VARCHAR({}) NOT NULL".format(self.max_length)
        
        # Both default and null are set
        elif self.default and not self.null:
            return "VARCHAR({}) DEFAULT '{}' NOT NULL".format(self.max_length, self.default)

        # No default or null is set
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
        # Only default is set
        if self.default:
            return "TEXT DEFAULT '{}'".format(self.default)
        
        # Only null is set
        elif not self.null:
            return "TEXT NOT NULL"
        
        # Both default and null are set
        elif self.default and not self.null:
            return "TEXT DEFAULT '{}' NOT NULL".format(self.default)

        # No default or null is set
        return "TEXT"
    
    def __repr__(self):
        # Only default is set
        if self.default:
            return "TEXT DEFAULT '{}'".format(self.default)
        
        # Only null is set
        elif not self.null:
            return "TEXT NOT NULL"
        
        # Both default and null are set
        elif self.default and not self.null:
            return "TEXT DEFAULT '{}' NOT NULL".format(self.default)

        # No default or null is set
        return "TEXT"
    
    def __eq__(self, other):
        return self.__dict__ == other.__dict__
