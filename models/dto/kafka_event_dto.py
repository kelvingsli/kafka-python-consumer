from .base_dto import BaseDto

class KafkaEventDto(BaseDto):

    def __init__(self, id=None, key=None, value=None):
        self.id = id
        self.key = key
        self.value = value

