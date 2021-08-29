from faker import Faker


class Name:
    def ru_name():
        fake = Faker('ru_RU')
        
        return fake.name()


    def en_name():
        fake = Faker('en_US')
        
        return fake.name()
