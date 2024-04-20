class BaseException(Exception):
    message: str = "Exception occured"

    def __str__(self):
        return self.message
