def get_input(msg):
    try:
        return input(msg)
    except ValueError:
        return ""


def get_int_input(msg):
    try:
        return int(input(msg))
    except ValueError:
        return 0


def get_double_input(msg):
    try:
        return float(input(msg))
    except ValueError:
        return 0.0
