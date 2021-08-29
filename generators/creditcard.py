from faker import Faker

Faker.seed(0)

class CreditCard:
    def ru_creditcard():
        fake = Faker('ru_RU')
        
        return fake.credit_card_full()
    
    def en_creditcard():
        fake = Faker('en_US')
        
        return fake.credit_card_full()
