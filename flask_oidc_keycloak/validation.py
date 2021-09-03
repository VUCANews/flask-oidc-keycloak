# Copyright (c) 2019, Lars Wilhelmsen <lars@sral.org>
# All rights reserved.
#
# Redistribution and use in source and binary forms, with or without
# modification, are permitted provided that the following conditions are met:
#
# * Redistributions of source code must retain the above copyright notice, this
#   list of conditions and the following disclaimer.
#
# * Redistributions in binary form must reproduce the above copyright notice,
#   this list of conditions and the following disclaimer in the documentation
#   and/or other materials provided with the distribution.
#
# THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS"
# AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE
# IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE
# DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT HOLDER OR CONTRIBUTORS BE LIABLE
# FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL
# DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR
# SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER
# CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY,
# OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE
# OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.

import python_jwt as jwt
import jwcrypto.jwk as jwk
import datetime

allowed_algs = [
  'RS256',
  'RS384',
  'RS512',
  'PS256',
  'PS384',
  'PS512',
  'ES256',
  'ES384',
  'ES512',
  'HS256',
  'HS384',
  'HS512']

def validate_token(jwkset, token, clock_skew_seconds):

    headers, _ = jwt.process_jwt(token)
    alg = headers['alg']
    kid = headers['kid']

    if not alg:
        raise Exception('No \'alg\' claim in JWT token header')
    
    if not alg in allowed_algs:
        raise Exception('\'%s\' is not an allowed algorithm.' % alg)

    if not kid:
        raise Exception('No \'kid\' claim in JWT token header')

    json_key = jwkset.get_key(kid)

    algorithms = [alg]

    # Exception raised on invalid token input will be bubble up to the caller.
    _, payload = jwt.verify_jwt(token, json_key, algorithms, datetime.timedelta(seconds=clock_skew_seconds))

    typ = payload.get('typ', None)
    if typ != 'Bearer':
       raise Exception('The token is not intended for autorization (\'typ\' should be \'Bearer\', not \'%s\')' % typ)

    return payload
