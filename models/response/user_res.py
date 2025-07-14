from flask_restx import fields, Namespace

# Namespace is required to define models
# This is just a placeholder; real namespace will provide this at runtime

def sample_one_res(ns: Namespace):
    return ns.model('Sample 1 Response', {
        'response_1': fields.String(description='String'),
        'response_2': fields.Boolean(description='Boolean')
    })

def sample_two_res(ns: Namespace):
    return ns.model('Sample 2 Response', {
        'response_1': fields.Integer(description='Integer')
    })

