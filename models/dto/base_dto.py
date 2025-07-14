import json

class BaseDto:

    def __str__(self):
        return json.dumps(
            self,
            default=lambda o: o.__dict__, 
            sort_keys=True
            )

    def __repr__(self):
        return json.dumps(
            self,
            default=lambda o: o.__dict__, 
            sort_keys=True
            )
