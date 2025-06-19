from prac_oop import Bank, customer, staff
import sys
import json

class BankFactory():

    @staticmethod
    def create_bank_entry(detail,name,pin,address,status,**kwargs):
        if detail.lower() == 'staff':
            return staff(name,pin,address,status,**kwargs)
        elif detail.lower() == 'customer':
            return customer(name,pin,address,status,**kwargs)
        else:
            print("Invalid detail! Please choose either 'staff' or 'customer'.")

def main():
    detail = sys.argv[1]
    name = sys.argv[2]
    pin = sys.argv[3]
    address = sys.argv[4]
    status = sys.argv[5]
    args = sys.argv[6:]

    input = {}
    for arg in args:
        key,value = arg.split("=")
        input[key]=value

    entry = BankFactory.create_bank_entry(detail,name,pin,address,status,**input)

    print("Entry Created:")
    print("ID:", entry.id)
    print("Name:", entry.name)
    print("Address:", entry.address)
    print("Balance:", entry.balance)
    print("Status:", entry.status)

    data = {
        entry.id: {'name': entry.name ,'address': entry.address,'balance': entry.balance,'status':entry.status
                   
        }
    }

    with open(f'{detail}.json', 'w') as f:
        json.dump(data, f, indent=4)

if __name__ == '__main__':
    main()