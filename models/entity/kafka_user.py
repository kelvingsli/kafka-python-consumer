from sqlalchemy import Column, Integer, String, Boolean, DateTime, func

from db.db_object import db

class KafkaUser(db.Model):
   
   __tablename__ = 'kafka_users'
   id = Column(Integer, primary_key=True)
   timestamp = Column(DateTime, default=func.now())
   key_id = Column(String(250), nullable=True)
   name = Column(String(250), nullable=True)
   is_registered = Column(Boolean, nullable=False)

