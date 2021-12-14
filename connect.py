#!/usr/bin/python
import psycopg2
from config import config
from prettytable import from_db_cursor


def connect():
    """ Connect to the PostgreSQL database server """
    conn = None
    try:
        params = config()
        print('Connecting to the PostgreSQL database...')
        conn = psycopg2.connect(**params)

        cur = conn.cursor()
        print('PostgreSQL database version:')
        cur.execute('SELECT version()')

        db_version = cur.fetchone()
        print(db_version)

        sql_file = open('wallet.sql', 'r')
        cur.execute(sql_file.read())

        sql_file_data = open('fake_data.sql', 'r')
        cur.execute(sql_file_data.read())

        conn.commit()
        cur.close()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()
            print('Database connection closed.')

def exec(command):
    try:
        params = config()
        conn = psycopg2.connect(**params)
        cur = conn.cursor()
        cur.execute(command)
        conn.commit()
        cur.close()
        return('Success')
    except (Exception, psycopg2.DatabaseError) as error:
        return error

def select_exec(command):
    conn = None
    try:
        params = config()
        conn = psycopg2.connect(**params)
        cur = conn.cursor()
        cur.execute(command)
        mytable = from_db_cursor(cur)
        cur.close()
        return mytable
    except (Exception, psycopg2.DatabaseError) as error:
        return error


if __name__ == "__main__":
    connect()