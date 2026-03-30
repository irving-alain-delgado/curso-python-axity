import re

EMAIL_PATTERN = r"^[\w\.-]+@[\w\.-]+\.\w+$"


def is_valid_email(email: str) -> bool:
    return bool(re.match(EMAIL_PATTERN, email))