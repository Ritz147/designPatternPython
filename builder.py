# text='hello'
# parts=['<p>',text,'</p>']
# print(''.join(parts))
# words=['hello','world']
# parts=['<ul>']
# for w in words:
#     parts.append(f'<li>{w}</li>')
# parts.append('</ul>')
# print('\n'.join(parts))
from abc import ABC, abstractmethod
class HtmlElement:
    indent_size=2
    def __init__(self , name='' , text=''):
        self.text=text
        self.name=name
        self.elements=[]
    def __str(self,indent):
        lines=[]
        i=' '*(indent*(self.indent_size))
        lines.append(f'{i} <{self.name}>')

        if self.text:
            i1=' '*((indent+1)*(self.indent_size))
            lines.append(f'{i1}{self.text}')
        for e in self.elements:
            lines.append(e.__str(indent+1))
        lines.append(f'{i}</{self.name}>')
        return '\n'.join(lines)
    def __str__(self):
        return self.__str(0)
    @staticmethod
    def create(name):
        return HTMLBuilder(name)
class HTMLBuilder:
    def __init__(self,root_name):
        self.root_name=root_name
        self.__root=HtmlElement(root_name)
    def add_child(self , child_name , child_text):
        self.__root.elements.append(HtmlElement(child_name,child_text))
    def add_child_fluent(self , child_name , child_text):
        self.__root.elements.append(HtmlElement(child_name,child_text))
        return self
    def __str__(self):
        return str(self.__root)
builder=HtmlElement.create('ul')
# builder.add_child('li','hello')
# builder.add_child('li','world')
builder.add_child_fluent('li','hello').add_child_fluent('li','world')
print('Ordinary Builder:')
print(builder)


class Person:
    def __init__(self):
        #address
        self.street_address=None
        self.postcode=None
        self.city=None
        #employment
        self.company_name=None
        self.position=None
        self.annual_income=None
    def __str__(self):
        return (f'Address:{self.street_address},{self.postcode},{self.city}\n Employed at {self.company_name} as a {self.postcode} earning {self.annual_income}')
class PersonBuilder:
    def __init__(self,person=Person()):
        self.person=person
    @property
    def works(self):
        return PersonJobBuilder(self.person)
    @property
    def lives(self):
        return PersonAddressBuilder(self.person)
    def build(self):
        return self.person
class PersonJobBuilder(PersonBuilder):
    def __init__(self , person=Person()):
        super().__init__(person)
    def at(self , company_name):
        self.person.company_name=company_name
        return self
    def as_a(self,position):
        self.person.position=position
        return self
    def earning(self , annual_income):
        self.person.annual_income=annual_income
        return self
class PersonAddressBuilder(PersonBuilder):
    def __init__(self,person):
        super().__init__(person)
    def at(self,street_address):
        self.person.street_address=street_address
        return self
    def with_postcode(self,postcode):
        self.person.postcode=postcode
        return self
    def in_city(self,city):
        self.person.city=city
        return self
pb=PersonBuilder()
person=pb\
.lives\
.at('123 London Road')\
.in_city('London')\
.with_postcode('SW12BC')\
.works\
.at('Fabrikam')\
.as_a('Engineer')\
.earning(123000)\
.build()
print(person)
