
# This is not a project ; just a practice for OOP


class Bank():
    def __init__(self, name, nid, age, balance):
        self.name = name
        self.nid = nid
        self.age = age
        self.balance = balance
        
        
    def UserDetails(self):
       # user = input("[#] Type username/ name of the client: ")
        # Pass = input("[#] Type password: ")
        print("User Details: ")
        print("[#] Name: " + self.name)
        print("[#] Age: " + str(self.age))
        print("[#] Balance: " + str(self.balance))

    
    
    def WithDraw(self, amount):
        if(amount <= self.balance):
            self.balance -= amount
            print("[#] Withdrawal Successfull")
        else:
            print("[#] You don't have suffiecient amount of balance")

    
    
    def Deposit(self, amount):
        self.balance += amount
        print("[#] Successfully deposited")

        
class User(Bank):
    def __init__(self, name, nid, age, balance):
        super().__init__(name, nid, age, balance)



user = User("Evan", 1000000, 25, 250000)
user.UserDetails()

