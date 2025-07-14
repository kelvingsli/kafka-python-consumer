from .base_dto import BaseDto

class KafkaUserDto(BaseDto):

    def __init__(self, id=None, timestamp=None, key_id=None, name=None, is_registered=None):
        self.id = id
        self.timestamp = timestamp
        self.key_id = key_id
        self.name = name
        self.is_registered = is_registered

