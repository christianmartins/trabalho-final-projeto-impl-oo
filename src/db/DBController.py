import sqlite3


def get_connection():
    return sqlite3.connect("../finalproject.db")


def get_cursor():
    return get_connection().cursor()


def execute_simple_query():
    return get_cursor()


def get_list(query):
    get_cursor().execute(query)
    return get_cursor().fetchall()
