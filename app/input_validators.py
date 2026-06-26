from app.exceptions import InvalidInputError


def validate_number(value):
    try:
        return float(value)
    except ValueError:
        raise InvalidInputError(f"Invalid number: {value}")


def validate_args(args):
    if len(args) != 2:
        raise InvalidInputError("Exactly 2 arguments required")
    return validate_number(args[0]), validate_number(args[1])