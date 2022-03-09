class Person:
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name
    def first_name(self):
        print(self.first_name)
class Jack(Person):
    def __init__(self, first_name, last_name, phone_number, balance):
        super().__init__(first_name, last_name)
        self.phone_number = phone_number
        self.balance = balance

class Vito(Jack):

    def __init__(self, first_name, last_name, phone_number, balance, number):
        self.number = number
        super().__init__(first_name, last_name, phone_number, balance)
    def nnn(self):
        Vito.balance = print(f'{Jack.balance - self.n}')
        print(f'{Vito.balance}')

    def transaction(self):
        print(f"Jack's balance: {Jack.balance - self.number}\nVito's balance: {Vito.balance + self.number}")

Jack = Jack('Jack', 'White', '123456', 2000)
Vito = Vito('Vito', 'Smith', '563212', 1400, 400)
Vito.transaction()