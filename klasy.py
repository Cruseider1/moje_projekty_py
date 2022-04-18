class pracownik:
    def __init__(self,name,pay):
        self.name = name
        self.pay = pay
    def lastName(self):
        return self.name.split()[-1]
    def giveRaise(self,percent):
        self.pay += (1.0 + percent)

bob = pracownik('Robert Zielony', 5000)
anna = pracownik('Anna Czerwona', 6000)

print(bob.lastName())
print(anna.lastName())

anna.giveRaise(10)

print(anna.pay)
