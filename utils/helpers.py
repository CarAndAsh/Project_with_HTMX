from flask import  request

def is_background_request():
    is_hx_req = request.headers.get('Hx-Request')
    return is_hx_req