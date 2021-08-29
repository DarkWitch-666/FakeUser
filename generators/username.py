import random

class UserName:
    def username():
        t = 'qwertyuiopasdfghjklzxcvbnm'
        h = "QWERTYUIOPASDFGHJKLZXCVBNM"
        g = "12345678910"
        
        nick = ""
        
        for i in range(3):
            nick += random.choice(t)
            nick += random.choice(h)
            nick += random.choice(g)
        
        return nick