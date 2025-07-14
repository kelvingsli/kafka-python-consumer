from models.dto.user_dto import UserOneDto, UserTwoDto

class UserService:

    def sample_one_process(self, param1, param2):
        response = UserOneDto(param1, param2)

        return response
    
    def sample_two_process(self, param1, param2):
        response = UserTwoDto(param1, param2)

        return response