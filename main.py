import jwt

data = {"language": "Python"}
secret = 'acelera'
token = b'eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJsYW5ndWFnZSI6IlB5dGhvbiJ9.sM_VQuKZe_VTlqfS3FlAm8XLFhgvQQLk2kkRTpiXq7M'


def create_token(data, secret):
    encoded_jwt = jwt.encode(data, secret, algorithm='HS256')
    return encoded_jwt


def verify_signature(token):
    try:
        docoded_jwt = jwt.decode(token, secret, algorithms='HS256')
        return docoded_jwt
    except jwt.exceptions.InvalidSignatureError:
        return {"error": 2}

