from abc import abstractclassmethod, ABC

class Person:

    def __init__(self, name):
        self.name = name
        
    def __repr__(self):
        return f'Person(name={self.name})'

class PersonStorage(ABC):
    
    @abstractclassmethod
    def save(cls, person):
        ...

class DatabaseStorage(PersonStorage):
    
    @classmethod    
    def save(cls, person):
        print(f'Save the {person} to database')


class JsonStorage(PersonStorage):

    @classmethod
    def save(cls, person):
        print(f'Save the {person} to a JSON file')



if __name__ == '__main__':
    person = Person('John Doe')
    storage = DatabaseStorage
    storage.save(person)