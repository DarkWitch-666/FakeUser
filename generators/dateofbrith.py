import random

class DateOfBrith:
    def dateofbrith():
        date = (f"{random.randint(1980, 2000)}.{random.randint(1, 12)}.{random.randint(1, 30)}")
        return date
