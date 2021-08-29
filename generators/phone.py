from faker import Faker

Faker.seed(0)

class Phone:
    def ru_phone():
        fake = Faker('ru_RU')
        
        return fake.phone_number()
    
    def en_phone():
        fake = Faker('en_US')
        
        return fake.phone_number()