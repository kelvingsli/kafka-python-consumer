import threading
import os
import logging

from utils.signal_setup import stop_flag
from logging.handlers import TimedRotatingFileHandler
from flask_migrate import Migrate
from flask import Flask
from routes import register_routes
from flask_restx import Api
from urllib.parse import quote_plus

from utils.kafka_consumer import create_consumer
from service.event_processing_svc import process
from db.db_object import db

def create_app():
    app = Flask(__name__)
    DB_URL = os.getenv('DB_URL')
    DB_USER = os.getenv('DB_USER')
    DB_PASSWORD = os.getenv('DB_PASSWORD')
    DB_DATABASE = os.getenv('DB_DATABASE')
    app.config['KAFKA_BROKER_URL']=os.getenv('KAFKA_BROKER_URL')
    app.config['KAFKA_SCHEMA_REGISTRY_URL']=os.getenv('KAFKA_SCHEMA_REGISTRY_URL')
    app.config['LOGPATH']=os.getenv('LOGPATH')
    app.config["SQLALCHEMY_DATABASE_URI"] = f'postgresql://{DB_USER}:{quote_plus(DB_PASSWORD)}@{DB_URL}/{DB_DATABASE}'
    app.config["KAFKA_BROKER_URL"] = os.getenv('KAFKA_BROKER_URL')
    # migrate = Migrate(app, db)
    setup_logger(app)
    db.init_app(app)
    migrate = Migrate(app, db)

    with app.app_context():
        from models.entity import wiki_event
        db.create_all()  # creates tables

    api = Api(app)
    register_routes(api)
    
    return app

def setup_logger(app:Flask):
    log_formatter = logging.Formatter(
        '%(asctime)s [%(levelname)s] %(name)s: %(message)s'
    )

    # === File handler ===
    file_handler = TimedRotatingFileHandler(
        app.config["LOGPATH"], when='midnight', interval=1, backupCount=7, encoding='utf-8'
    )
    file_handler.setFormatter(log_formatter)
    file_handler.setLevel(logging.INFO)

    # === Console handler ===
    console_handler = logging.StreamHandler()
    console_handler.setFormatter(log_formatter)
    console_handler.setLevel(logging.INFO)

    root_logger = logging.getLogger()  # this is the global root logger

    # Clear existing handlers (optional)
    if root_logger.hasHandlers():
        root_logger.handlers.clear()

    root_logger.setLevel(logging.INFO)
    root_logger.addHandler(file_handler)
    root_logger.addHandler(console_handler)

    # Optional: redirect werkzeug logs too
    # logging.getLogger('werkzeug').addHandler(file_handler)
    logging.info(f'App config: {app.config["LOGPATH"]}')


