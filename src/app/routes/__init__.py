
from .home import home_routes
from .things import things_routes


def register_routes(app): 
    app.register_blueprint(home_routes)
    app.register_blueprint(things_routes)
