class Dog:
    
    tricks = []
    
    def __init__(self, name):
        self.name = name

        
if __name__ == '__main__':
    
    fido = Dog(name='fido')
    print(fido.tricks)
    milou = Dog(name='milou')
    print(milou.tricks)
    fido.tricks.append('run')
    print(fido.tricks)
    milou.tricks = []
    milou.tricks.append('sleep')
    print(milou.tricks)
    print(fido.tricks)
    
    
