class UndefinedSystemException(Exception):
    def __init__(self, message, execution_time):
        super().__init__(message)
        self.execution_time = execution_time