class Task:

    def __init__(self, message: str):
        self.message: str = message
        self.done: bool = False

    def get_message(self) -> str:
        return self.message
    
    def set_done(self) -> None:
        self.done = True