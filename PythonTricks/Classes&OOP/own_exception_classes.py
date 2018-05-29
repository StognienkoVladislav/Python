
class NameTooShortError(ValueError):
    pass


def validate(name):
    if len(name) < 10:
        raise NameTooShortError(name)


print(validate('joe'))