import os
import psycopg
from psycopg_pool import ConnectionPool
from flask import g
from flask_migratepg import MigratePg

from .config import Config


def register_db(app):

    connection_pool = ConnectionPool(
        min_size=1,
        max_size=5,
        conninfo=f"host={Config.DB_HOST} port={Config.DB_PORT} dbname={Config.DB_NAME} user={Config.DB_USER} password={Config.DB_PASSWORD}"
    )

    @app.before_request
    def before_request():
        """Assign a connection before handling the request."""
        g.db_connection = connection_pool.getconn()
        g.db_connection.row_factory = psycopg.rows.dict_row

    @app.after_request
    def after_request(response):
        """Release the connection back to the pool."""
        connection_pool.putconn(g.db_connection)
        return response

    app.config.from_mapping(
        MIGRATIONS_PATH=os.path.abspath('src/database/migrations'),
        PSYCOPG_CONNINFO=f"dbname={Config.DB_NAME} host={Config.DB_HOST} port={Config.DB_PORT} user={Config.DB_USER} password={Config.DB_PASSWORD}"
    )
    MigratePg(app)
