import logging
from flask_restx import Resource, Namespace

from models.request.kafka_req import send_req
from models.response.kafka_res import send_res

ns = Namespace('kafka', description='Kafka operations')

send_req_model = send_req(ns)
send_res_model = send_res(ns)

@ns.route('/')
class Kafka(Resource):
    def get(self):
        return {'user': 'hello world'}

@ns.route('/send')
class KafkaSend(Resource):

    @ns.expect(send_req_model)
    @ns.marshal_with(send_res_model)
    def post(self):
        return {}, 200