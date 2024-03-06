class BaseAppError(Exception):
    def __init__(self, msg: str = ""):
        self.msg = msg
        super().__init__(self.msg)


class WrongInputError(BaseAppError):
    pass


class NotFoundError(BaseAppError):
    pass


class RemoteServerTimeoutError(BaseAppError):
    pass


class RemoteServerInternalError(BaseAppError):
    pass
