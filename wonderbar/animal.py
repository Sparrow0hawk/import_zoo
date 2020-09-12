import sys 

sys.path.append('wonderbar')

from zookeeper import Zookeeper

class Animal:
    
    def __init__(self, name : str, keeper : str) -> None:
        self.name = name
        self.keeper = Zookeeper(keeper)

    def get_name(self):
        return self.name 

    def get_keeper(self):
        return self.keeper.name

    
if __name__ == '__main__':
    
    big_cat = Animal(name = 'leo', keeper = 'Tracey')

    print(big_cat.get_name())
