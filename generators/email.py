from faker import Faker

Faker.seed(0)

class Email:
    def ru_email():
        fake = Faker('ru_RU')
        
        return fake.email()
    
    def en_email():
        fake = Faker('en_US')
        
        return fake.email()