class Market:
    marketCount = 0
    def __init__(self, name, year):
        self.name = name
        self.year = year
        Market.marketCount += 1
        print('Created new Market!!',name)

    def get_name(self):
        return self.name

    def set_name(self,name):
        self.name = name

m = Market('555',2499)
print(m.get_name())
m.set_name('Ohaiyo Farm')
print(m.get_name())
n = Market('OHOHO',2563)
print('Market Count = ',Market.marketCount)