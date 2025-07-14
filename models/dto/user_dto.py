from .base_dto import BaseDto

class UserOneDto(BaseDto):

    def __init__(self, param1=None, param2=None):
        self.param1 = param1
        self.param2 = param2


class UserTwoDto(BaseDto):

    def __init__(self, param1=None, param2=None):
        self.param1 = param1
        self.param2 = param2

