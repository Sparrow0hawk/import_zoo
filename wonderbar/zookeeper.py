
from os import name


class Zookeeper:

    def __init__(self, name : str) -> None:
        self.name = name 

    def get_name(self):
        return self.name