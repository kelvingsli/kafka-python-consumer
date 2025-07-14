from .users import ns as ns_users
from .products import ns as ns_products
from .kafka import ns as ns_kafka

def register_routes(api):
    api.add_namespace(ns_users)
    api.add_namespace(ns_products)
    api.add_namespace(ns_kafka)