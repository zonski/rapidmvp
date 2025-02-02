from flask import Blueprint, render_template, g, request

things_routes = Blueprint('things', __name__)


@things_routes.route('/things', methods=['GET'])
def list_things():
    with g.db_connection.cursor() as cursor:    
        cursor.execute("SELECT id, name, description from thing;")
        things = cursor.fetchall()
        return render_template(
            "things/list-things.html",
            things=things
        )

@things_routes.route('/things/create', methods=['GET'])
def create_thing():
    return render_template(
        "things/create-thing.html",
    )

@things_routes.route('/things/create', methods=['POST'])
def create_thing_post():
    name = request.form.get('name')
    description = request.form.get('description')
    print(f"Name: {name}, Description: {description}")
    with g.db_connection.cursor() as cursor:
        cursor.execute("INSERT INTO thing (name, description) VALUES (%s, %s);", (name, description))
        g.db_connection.commit()
    return "Thing created"
