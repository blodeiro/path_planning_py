class Robot:
    def __init__(self, params : dict) -> None:
        self.config = params
        self.status = {}
    
    def hello(self):
        return "hello"