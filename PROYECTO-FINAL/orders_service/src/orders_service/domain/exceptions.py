class DomainError(Exception):
    """Base class for domain errors."""
    pass


class InvalidQuantityError(DomainError):
    pass