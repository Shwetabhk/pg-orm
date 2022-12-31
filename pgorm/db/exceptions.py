"""
All PGORM Exceptions are defined here
"""

class PGORMException(Exception):
    """
    Base PGORM Exception
    """
    def __init__(self, message: str):
        self.message = message
        super().__init__(self.message)


class RecordNotFound(PGORMException):
    """
    Record Not Found Exception
    """
    def __init__(self, message: str):
        super().__init__(message)


class MigrationError(PGORMException):
    """
    Migration Error Exception
    """
    def __init__(self, message: str):
        super().__init__(message)
