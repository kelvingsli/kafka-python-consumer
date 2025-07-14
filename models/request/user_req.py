from flask_restx import fields, Namespace

# Namespace is required to define models
# This is just a placeholder; real namespace will provide this at runtime

def sample_one_req(ns: Namespace):
    return ns.model('Auth Request', {
        'param_str': fields.String(required=True, description='Sample string'),
        'param_bool': fields.Boolean(required=True, description='Sample boolean')
    })

def sample_two_req(ns: Namespace):
    return ns.model('Refresh Request', {
        'param_int1': fields.Integer(required=True, description='Sample integer 1'),
        'param_int2': fields.Integer(required=True, description='Sample integer 2')
    })