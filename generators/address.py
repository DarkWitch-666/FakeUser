from faker import Faker

Faker.seed(0)

class Address:
    def ru_address():
        fake = Faker('ru_RU')
        
        return fake.address()

    def en_address():
        fake = Faker('en_US')
        
        return fake.address()
