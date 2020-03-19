def get_int_input(msg):
    try:
        return int(input(msg))
    except ValueError:
        return 0
