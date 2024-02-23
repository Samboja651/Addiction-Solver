# from app import db
import sqlite3

import click
from flask import current_app, g  
# g is used to store data that might be accessed by multiple functions during a request, the conn is stored and reused

def get_db():
    if 'db' not in g:
        g.db = sqlite3.connect(
            current_app.config['DATABASE'],
            detect_types = sqlite3.PARSE_DECLTYPES
        )
        g.db.row_factory = sqlite3.Row # tells the connection to return rows that behave like dicts. it allows accessing the columns by names
    return g.db

def close_db(e = None):
    # if g.db was set, the connection exists and it is closed
    db = g.pop('db', None)

    if db is not None:
        db.close()


def init_db():
    db = get_db()

    with current_app.open_resource('schema.sql') as schema:
        db.executescript(schema.read().decode('utf8'))


@click.command('init-db')
def init_db_command():
    """create new tables if they don't exist."""
    init_db()
    click.echo('Initialized the database.')


def init_app(app):
    app.teardown_appcontext(close_db)
    app.cli.add_command(init_db_command)

