from flask_oidc_keycloak.jwks import retrieve_jwks
from nose.tools import nottest
from httplib2 import Http

from flask_oidc_keycloak.discovery import discover_OP_information

jwks_url = 'https://www.googleapis.com/oauth2/v3/certs'


@nottest
def http_factory_ssl_cert_validation_disabled():
    return Http(disable_ssl_certificate_validation=True)


def test_can_retrieve_jwks_from_google():
    jwkset = retrieve_jwks(jwks_url, http_factory_ssl_cert_validation_disabled)
    assert jwkset is not None
