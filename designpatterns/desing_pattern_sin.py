class Teacher:
    
    instance = None
    
    def __init__(self, name):
        self.__name = name
    
    @classmethod
    def get_instance(cls):
        # verifier si instance est deja attribuee
        # si encore a None, alors creer une nouvelle instance de Teacher
        if cls.instance is None:
            cls.instance = Teacher('a')
        return cls.instance
        
    def __str__(self):
        return f'{self.__class__.__name__}: {self.__name}'
        
if __name__ == '__main__':
    a = Teacher.get_instance()
    a_copy = Teacher.get_instance()
    b = Teacher('b')
    print(a, a_copy)
    assert a == a_copy
    assert isinstance(a, Teacher)
    assert isinstance(a_copy, Teacher)
    assert a == b