def is_a_valid_key(body: dict):
    KEYS_USER = ["nome", "email"]
    KEYS_USER.sort()
    check_keys = list(body.keys())
    check_keys.sort()

    if KEYS_USER == check_keys:
        return True

    return False


def is_a_valid_values(body: dict):
    TYPE_VALUES_KEYS = str
    check_values = body.values()

    for value in check_values:
        if type(value) != str:
            return False

    return True
