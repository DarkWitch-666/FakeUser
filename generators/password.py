import random

class Password:
    def password():
        t = 'qwertyuiopasdfghjklzxcvbnm'
        h = "QWERTYUIOPASDFGHJKLZXCVBNM"
        g = "12345678910"
        
        password = ""
        
        for i in range(3):
            password += random.choice(t)
            password += random.choice(h)
            password += random.choice(g)
        
        return password