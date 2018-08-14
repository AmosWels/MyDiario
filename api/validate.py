"""importing regular expressions class"""
import re


class Validate():
    """valiation class for diary inputs"""
    def __init__(self, username,password,):
        self.username = username
        self.password = password

    def validate_entry(self):
        """method to validate inputs"""
        result = ""
        if(not re.search("[a-zA-Z0-9]", self.username) or not
                re.search("[a-zA-Z0-9]", self.password)):
            result = "INCORRECT INPUT OR EMPTY INPUT. NAME AND PURPOSE SHOULD BE PROVIDED!"
        else:
            result = True
        return result

    def validate_field(data,required_fields):
        for field in required_fields:
            if field not in data:
                return {
                    "success":False,
                    "message": '*' + field + '*' +' is required before operation' }
            
            
