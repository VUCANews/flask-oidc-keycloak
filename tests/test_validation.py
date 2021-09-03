from flask_oidc_keycloak.validation import validate_token
from nose.tools import assert_raises
from python_jwt import generate_jwt, verify_jwt
from jwcrypto.jwk import JWK, JWKSet
import datetime

key = JWK.generate(kty='RSA', size=1024, kid='1234')

def test_validate_token():

    payload = {'typ': 'Bearer', 'foo': 'bar', 'baz': 42}
    other_headers = {'kid': key.key_id}

    token = generate_jwt(payload, key, 'RS256', datetime.timedelta(minutes=5), other_headers=other_headers)
    header, claims = verify_jwt(token, key, ['RS256'])

    assert header is not None
    assert claims is not None

    keyset = JWKSet()
    keyset.add(key)

    assert validate_token(keyset, token, clock_skew_seconds=60)

def test_will_raise_exception_when_typ_is_not_Bearer():
    payload = {'typ': 'ID', 'foo': 'bar', 'baz': 42}
    other_headers = {'kid': key.key_id}

    token = generate_jwt(payload, key, 'RS256', datetime.timedelta(minutes=5), other_headers=other_headers)
    assert_raises(Exception, verify_jwt(token, key, ['RS256']))

