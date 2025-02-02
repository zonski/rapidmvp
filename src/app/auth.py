from authlib.integrations.flask_client import OAuth
from flask import redirect, url_for, session
from urllib.parse import quote_plus, urlencode

from .config import Config

def register_auth(app):
    oauth = OAuth(app)
    app.oauth = oauth

    oauth.register(
        "auth0",
        client_id=Config.AUTH0_CLIENT_ID,
        client_secret=Config.AUTH0_CLIENT_SECRET,
        client_kwargs={
            "scope": "openid profile email",
        },
        server_metadata_url=f'https://{Config.AUTH0_DOMAIN}/.well-known/openid-configuration'
    )

    @app.route("/login")
    def login():
        return oauth.auth0.authorize_redirect(
            redirect_uri=url_for("callback", _external=True),
        )

    @app.route("/login-otp")
    def login_otp():
        return oauth.auth0.authorize_redirect(
            redirect_uri=url_for("callback", _external=True),
            connection="email",
        )
        
    @app.route("/callback", methods=["GET", "POST"])
    def callback():
        token = oauth.auth0.authorize_access_token()
        session["user"] = token
        return redirect("/")

    @app.route("/logout")
    def logout():
        session.clear()
        return redirect(
            "https://" + Config.AUTH0_DOMAIN
            + "/v2/logout?"
            + urlencode(
                {
                    "returnTo": url_for("home.show_home", _external=True),
                    "client_id": Config.AUTH0_CLIENT_ID,
                },
                quote_via=quote_plus,
            )
        )
