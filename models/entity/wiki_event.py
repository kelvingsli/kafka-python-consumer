from sqlalchemy import Column, Integer, String, DateTime

from db.db_object import db

class KafkaWikiPost(db.Model):
   
   __tablename__ = 'kafka_wiki_posts'
   id = Column(Integer, primary_key=True)
   key_id = Column(String(250), unique=True, nullable=False)
   timestamp = Column(DateTime, nullable=True)
   title = Column(String(2000), nullable=True)
   title_url = Column(String(2000), nullable=True)
   source = Column(String(250), nullable=True)

