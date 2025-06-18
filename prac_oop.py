import json
from abc import ABC, abstractmethod

def balance_v(func):
    def wrapper(self, amount, *args):
        if amount > self.balance:
            print("Insufficient balance.")
            return False
        return func(self, amount, *args)
    return wrapper
def check_datatype(data_type):
    def check_value(func):
        def wrapper(*args):
            if not isinstance(args[1], data_type):
                print(f"Not valid. Amount must be of type {data_type}")
                return False
            return func(*args)
        return wrapper
    return check_value
class Bank(ABC):
    @abstractmethod
    def deposit(self):
        pass
    @abstractmethod
    def withdraw(self):
        pass
    bank_name = 'Nabil Bank'
    def __init__(self):
        self.id = id(self)
        self.name = None
        self.__pin = None
        self.balance = 0
        self.address = None
        self.type = 'cust'
    @abstractmethod
    def bank_balance(self):
        pass
class customer(Bank):
    def __init__(self, name, pin, address,status):
        super().__init__()
        self.name = name
        self.__pin = pin
        self.address = address
        self.type = "customer"
        self.status = status
    def bank_balance(self):
        print(f"{self.name}'s balance: {self.balance}")
    @check_datatype(int)
    def deposit(self, amount):
        print(f"Deposited: {amount}")
        self.balance += amount
        print(f"Current Balance: {self.balance}")
    @check_datatype(int)
    @balance_v
    def withdraw(self, amount):
        print(f"Withdrawn: {amount}")
        self.balance -= amount
        print(f"Current Balance: {self.balance}")
    @check_datatype(int)
    @balance_v
    def transfer_mon(self,amount,receiver):
        self.balance -= amount
        receiver.balance += amount
        print(f" {amount} sent to {receiver.name}. Balance: {self.balance}")

    def change_pin(self,old_pin,new_pin):
        if self.__pin == old_pin:
            self.__pin == new_pin
            print(f'pin changed successfully for {self.name}')
        else:
            print(f'pin not changed for {self.name}')
    
 

class staff(Bank):
    def __init__(self, name, pin, address, department):
        super().__init__()
        self.name = name
        self.pin = pin
        self.address = address
        self.department = department
        self.type = 'staff'
    def bank_balance(self):
        print(f"Staff {self.name}'s balance: {self.balance}")
    @check_datatype(int)
    def deposit(self, amount):
        print(f"Deposited: {amount}")
        self.balance += amount
        print(f"Current Balance: {self.balance}")
    @check_datatype(int)
    @balance_v
    def withdraw(self, amount):
        print(f"Withdrawn: {amount}")
        self.balance -= amount
        print(f"Current Balance: {self.balance}")

    @check_datatype(int)
    @balance_v
    def transfer_mon(self,amount,receiver):
        self.balance -= amount
        receiver.balance += amount
        print(f" {amount} sent to {receiver.name}. Balance: {self.balance}")

cust1 = customer("Luffy", 1111, "Kathmandu","Active")
cust2 = customer("Zoro", 2222, "Patan","Active")
cust1.deposit(1000)
cust1.withdraw(300)
cust1.bank_balance()
print()
stff1 = staff("Nami", 3333, "bhaktapur", "Accounts")
stff2 = staff("Vivi", 4444, "sunsari", "Accounts")
stff1.deposit(2000)
stff1.withdraw(500)
stff1.bank_balance()

cust1.transfer_mon(400,cust2)
stff1.transfer_mon(400,stff2)

cust1.change_pin('1110','9999')
cust1.change_pin('1111','9999')

data = {}
data[cust1.id] = {'name':cust1.name, 'address':cust1.address,'status':cust1.status}
with open('customer.json','w') as f:
    json.dump(data, f, indent=4)

data = {}
data[stff1.id] = {'name':stff1.name, 'address':stff1.address}
with open('staff.json','w') as f:
    json.dump(data, f, indent=4)
