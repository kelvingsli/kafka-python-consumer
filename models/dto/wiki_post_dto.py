from .base_dto import BaseDto

class WikiPostDto(BaseDto):

    def __init__(self, id=None, key_id=None, title=None, title_url=None, timestamp=None, source=None):
        self.id = id
        self.key_id = key_id
        self.title = title
        self.title_url = title_url
        self.timestamp = timestamp
        self.source = source
