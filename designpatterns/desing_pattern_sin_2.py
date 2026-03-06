class TeacherSingleton(type):

    instance = None
    
    def __call__(cls, *args, **kwargs):
        if cls.instance is None:
            cls.instance = super().__call__(*args, **kwargs)
        return cls.instance


class Teacher(metaclass=TeacherSingleton):

    def __init__(self, name):
        self.__name = name
            
    def __str__(self):
        return f'{self.__class__.__name__}: {self.__name}'
        
if __name__ == '__main__':
    a = Teacher('a')
    a_copy = Teacher('a')
    b = Teacher('b')
    print(a, a_copy)
    assert a == a_copy
    assert isinstance(a, Teacher)
    assert isinstance(a_copy, Teacher)
    assert a == b