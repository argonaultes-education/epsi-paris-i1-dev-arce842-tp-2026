from abc import ABC, abstractmethod

class Contact:
    
    def __init__(self, email, phone, discordid):
        self.email = email
        self.phone = phone
        self.discordid = discordid

class Notification(ABC):
    
    def __init__(self, contact:Contact):
        self.contact = contact

    @abstractmethod
    def notify(self, message):
        pass

class Email(Notification):
    
    def __init__(self, contact:Contact):
        super().__init__(contact)
    
    def notify(self, message):
        print(f'Send {message} to {self.contact.email}')

class SMS(Notification):

    def __init__(self, contact:Contact):
        super().__init__(contact)
    
    def notify(self, message):
        print(f'Send {message} to {self.contact.phone}')

class Discord(Notification):
    
    def __init__(self, contact:Contact):
        super().__init__(contact)
        
    def notify(self, message):
        print(f'Discord message {message} notification to {self.contact.discordid}')

if __name__ == '__main__':
    john_contact = Contact(email='j@john.com', phone='12345', discordid='john')
    notification = Discord(john_contact)
    notification.notify('Hello')