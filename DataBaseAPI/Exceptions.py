class UserNotFoundError(Exception):
    def __init__(self):
        self.message = "User with such user id not found"
        super().__init__(self.message)