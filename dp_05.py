from enum import Enum
from abc import abstractmethod
class Relationship(Enum):
    PARENT=0
    CHILD=1
    SIBLING=2
class Person:
    def __init__(self,name):
        self.name=name
class RelationshipBrowser():
    @abstractmethod
    def find_all_children(self,name):
        pass
class Relationships(RelationshipBrowser):#low level module
    def __init__(self):
        self.relations=[]
    def add_parent_and_child(self,parent,child):
        self.relations.append([parent,Relationship.PARENT,child])
        self.relations.append([child,Relationship.CHILD,parent])
    def find_all_children(self,name):
        for r in self.relations:
            if r[0].name==name and r[1]==Relationship.PARENT:
                yield r[2].name
class Research:#high level module
    def __init__(self,browser):
        for p in browser.find_all_children('John'):
            print(f'John has a child called {p}')
        
parent=Person('John')
child1=Person('Chris')
child2=Person('Matt')
relationships=Relationships()
relationships.add_parent_and_child(parent,child1)
relationships.add_parent_and_child(parent,child2)
research=Research(relationships)


