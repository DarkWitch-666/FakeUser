from faker import Faker

Faker.seed(0)

class Coordinate:
    def ru_coordinate():
        fake = Faker('ru_RU')
        
        return fake.coordinate()
    
    def en_coordinate():
        fake = Faker('en_US')
        
        return fake.coordinate()
