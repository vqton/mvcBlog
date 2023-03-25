import click
from flask import current_app, cli
from flask.cli import with_appcontext
from app import db

@click.command(name="initdb")
@with_appcontext
def initdb_command():
    """Initialize the database."""
    db.create_all()
    click.echo('Initialized the database.')

@click.command(name="dropdb")
@with_appcontext
def dropdb_command():
    """Drop the database."""
    db.drop_all()
    click.echo('Dropped the database.')

# add cli commands to app
def init_app(app):
    app.cli.add_command(initdb_command)
    app.cli.add_command(dropdb_command)
