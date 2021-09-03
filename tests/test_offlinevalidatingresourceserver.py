from flask import Flask
from flask_oidc_keycloak import OfflineValidatingResourceServer


def test_can_init():
    app = Flask(__name__)
    oidc = OfflineValidatingResourceServer(app, "https://accounts.google.com/.well-known/openid-configuration")
    assert oidc
