from sqlalchemy import Column, Integer, String

from db.db_object import db

class KafkaEvent(db.Model):
   
   __tablename__ = 'kafka_events'
   id = Column(Integer, primary_key=True)
   key = Column(String(250), nullable=True)
   value = Column(String(250), nullable=False)

