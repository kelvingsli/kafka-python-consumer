import logging
from sqlalchemy.dialects.postgresql import insert

from db.db_object import db
from models.entity.wiki_event import KafkaWikiPost
from models.dto.wiki_post_dto import WikiPostDto

class KafkaWikiStore:

    def get_wiki_post(self, post_id) -> WikiPostDto:
        wikipost = KafkaWikiPost()
        wikipost = db.one_or_404(db.select(wikipost).filter_by(id=post_id))
        return WikiPostDto(id=wikipost.id, key_id=wikipost.key_id, title=wikipost.title, title_url=wikipost.title_url, 
                        timestamp=wikipost.timestamp, source=wikipost.source)

    def create_wiki_post(self, key_id, title, title_url, timestamp, source) -> WikiPostDto:
        wikipost = KafkaWikiPost()
        wikipost.key_id = key_id
        wikipost.title = title
        wikipost.title_url = title_url
        wikipost.timestamp = timestamp
        wikipost.source = source
        db.session.add(wikipost)
        db.session.commit()
        return WikiPostDto(id=wikipost.id, key_id=wikipost.key_id, title=wikipost.title, title_url=wikipost.title_url, 
                        timestamp=wikipost.timestamp, source=wikipost.source)
    
    '''
    Insert if new record based on key_id unique constraints, update if key_id already exists
    '''
    def upsert_wiki_post(self, key_id, title, title_url, timestamp, source) -> WikiPostDto:
        
        stmt = insert(KafkaWikiPost).values(
            key_id=key_id,
            title=title,
            title_url=title_url,
            timestamp=timestamp,
            source=source
        )
        
        # Define update if conflict on another_id
        on_conflict_stmt = stmt.on_conflict_do_update(
            index_elements=['key_id'],  # assumes unique constraint/index
            set_={
                'title': title,
                'title_url': title_url,
                'timestamp': timestamp,
                'source': source
            }
        ).returning(KafkaWikiPost)

        result = db.session.execute(on_conflict_stmt)
        db.session.commit()

        wikipost = result.scalar_one()

        return WikiPostDto(id=wikipost.id, key_id=wikipost.key_id, title=wikipost.title, title_url=wikipost.title_url, 
                        timestamp=wikipost.timestamp, source=wikipost.source)
    
