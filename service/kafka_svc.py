import datetime

from repository.kafka_wiki_store import KafkaWikiStore as kafka_wiki_store
from models.dto.wiki_post_dto import WikiPostDto
from models.proto.wikipost_pb2 import WikiPost

class KafkaService:
    
    def save(self, key:str, wikipost:WikiPost) -> WikiPostDto:
        timestamp = datetime.datetime.fromtimestamp(int(wikipost.timestamp))
        new_post = kafka_wiki_store().upsert_wiki_post(key, wikipost.title, wikipost.title_url, timestamp, wikipost.source)
        return new_post
    