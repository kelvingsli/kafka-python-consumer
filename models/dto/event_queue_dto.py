from .base_dto import BaseDto

class EventQueueItem(BaseDto):

    def __init__(self, key=None, value=None):
        self.key = key
        self.value = value

