import logging
from flask_restx import Resource, Namespace

from service.user_svc import UserService as user_svc
from models.request.user_req import sample_one_req, sample_two_req
from models.response.user_res import sample_one_res, sample_two_res

ns = Namespace('users', description='User operations')

sample_one_req_model = sample_one_req(ns)
sample_two_req_model = sample_two_req(ns)

sample_one_res_model = sample_one_res(ns)
sample_two_res_model = sample_two_res(ns)

@ns.route('/')
class User(Resource):
    def get(self):
        return {'user': 'hello world'}

@ns.route('/sample1')
class UserSample1(Resource):

    @ns.expect(sample_one_req_model)
    @ns.marshal_with(sample_one_res_model)
    def post(self):
        logging.info("Starting sample 1 endpoint logic...")
        result = user_svc().sample_one_process(ns.payload['param_str'], ns.payload['param_bool'])
        response = response = {
            'response_1': result.param1,
            'response_2': result.param2
        }
        return response, 200

@ns.route('/sample2')
class UserSample2(Resource):

    @ns.expect(sample_two_req_model)
    @ns.marshal_with(sample_two_res_model)
    def post(self):
        response = {
            'response_1': 'ok'
        }
        return response, 200
