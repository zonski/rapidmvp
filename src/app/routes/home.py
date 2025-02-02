import json
from flask import session, Blueprint, render_template

home_routes = Blueprint('home', __name__)


@home_routes.route('/')
def show_home():
    return render_template(
        "home/home.html",
        session=session.get('user'),
        pretty=json.dumps(session.get('user'), indent=4)
    )
