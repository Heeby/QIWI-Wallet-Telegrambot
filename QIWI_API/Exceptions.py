
class InvalidQIWILoginDataError(Exception):
    def __init__(self):
        self.message = "Phone and token you send is incorrect"
        super().__init__(self.message)