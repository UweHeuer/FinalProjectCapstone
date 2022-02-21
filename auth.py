import json
import os
from flask import request, _request_ctx_stack
from functools import wraps
from jose import jwt
from urllib.request import urlopen

AUTH0_DOMAIN = os.environ.get('AUTH0_DOMAIN')
ALGORITHMS = os.environ.get('ALGORITHMS')
API_AUDIENCE = os.environ.get('API_AUDIENCE')

class AuthError(Exception):
    '''
    Exception to standardize auth failures
    '''
    def __init__(self, error, status_code):
        self.error = error
        self.status_code = status_code



def get_token_auth_header():
    '''
    - gets the header from the request
    - raises an AuthError if no header is present
    - splits bearer and token
    - raises an AuthError if header malformed
    - returns the token
    '''

    # get authorization header
    auth_header = request.headers.get("Authorization", None)
    if not auth_header:
        # authorization header missing => return error details and HTTP code 'unauthorized'
        raise AuthError({
            'code': 'authorization_header_missing',
            'description': 'authorization header is missing'
            },
            401)

    auth_header_parts = auth_header.split(' ')       
    
    if (len(auth_header_parts) != 2):
        # header format wrong
        raise AuthError({
            'code': 'wrong_authorization_header_format',
            'description': 'invalid authorization header'
        },
        401) 

    if ('bearer' != auth_header_parts[0].lower()):
        # bearer missing
        raise AuthError({
            'code': 'missing_bearer_in_authorization_header',
            'description': 'no bearer in authorization header'
        },
        401)  

    # return bearer token
    return auth_header_parts[1]    

def check_permissions(permission, payload):
    '''
    - raises an AuthError in no permissions in payload
    - raises an AuthError if requested permission string is not in payload permission
    - returns True if everything is ok
    '''

    # print("Permissions of payload are " + str(payload['permissions']))

    if 'permissions' not in payload:
        raise AuthError({
            'code': 'invalid_payload',
            'description': 'permissions not included in payload'
        }, 
        401)

    if permission not in payload['permissions']:
        raise AuthError({
            'code': 'unauthorized',
            'description': 'unauthorized'
        }, 
        401)

    return True


def verify_decode_jwt(token):
    '''
    - checks Auth0 token key
    - verifies token
    - decode the payload from token
    - validates claim
    - returns the decoded payload
    '''

    # see tutorial at https://auth0.com/docs/quickstart/backend/python/01-authorization
    # get the json web key set
    jsonurl = urlopen(f'https://{AUTH0_DOMAIN}/.well-known/jwks.json')    
    jwks = json.loads(jsonurl.read())
    try:
        unverified_header = jwt.get_unverified_header(token)
    except jwt.JWTError:
        raise AuthError({
            'code': 'invalid_token',
            'description': 'token is invalid'
            }, 
            401)          

    
    rsa_key = {}
    for key in jwks["keys"]:
        if key["kid"] == unverified_header["kid"]:
            rsa_key = {
                "kty": key["kty"],
                "kid": key["kid"],
                "use": key["use"],
                "n": key["n"],
                "e": key["e"]
            }
    if rsa_key:
        try:
            payload = jwt.decode(
                token,
                rsa_key,
                algorithms = ALGORITHMS,
                audience = API_AUDIENCE,
                issuer = 'https://' + AUTH0_DOMAIN + '/'
            )

            return payload

        except jwt.ExpiredSignatureError:
            raise AuthError({
                'code': 'token_expired',
                'description': 'token has expired'
                }, 
                401)  

        except jwt.JWTClaimsError:
            raise AuthError({
                'code': 'invalid_claims',
                'description': 'invalid claims'
                }, 
                401)         

        except Exception:
            raise AuthError({
                'code': 'invalid_token',
                'description': 'invalid token'
            }, 
            401)                       

    raise AuthError({
        'code': 'invalid_header',
        'description': 'unable to find the appropriate key'
        }, 
        401)


def requires_auth(permission=''):
    '''
    - uses the methods above
    - returns the decorator
    '''
    def requires_auth_decorator(f):
        @wraps(f)
        def wrapper(*args, **kwargs):
            token = get_token_auth_header()
            payload = verify_decode_jwt(token)
            check_permissions(permission, payload)
            return f(payload, *args, **kwargs)

        return wrapper
    return requires_auth_decorator