from flask_restx import fields, Namespace

# Namespace is required to define models
# This is just a placeholder; real namespace will provide this at runtime

def send_res(ns: Namespace):
    return ns.model('Send Call Response', {
        'result': fields.String(description='Result'),
        'error': fields.Boolean(description='Error')
    })


