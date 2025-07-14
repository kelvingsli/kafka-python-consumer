from flask_restx import Resource, Namespace

ns = Namespace('products', description='Product operations')

@ns.route('/products')
class Product(Resource):
    def get(self):
        return {'product': 'hello world'}
