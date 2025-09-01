class circumference:
    def __init__(self):
        while True:
            try:
                self.radius = int(input("Enter the radius of the circle: "))
                break
            except ValueError:
                print("Invalid input. Please enter a valid number.")
    def calculateCircumference(self):
        return 2* 3.14 * self.radius
obj = circumference()
print(obj.calculateCircumference())




class BankAccount:
    def __init__(self):
        self.accountNumber = input("Enter your account number: ")
        self.balance = 0
    def info(self):
        print(f"Account Number: {self.accountNumber}\nBalance: {self.balance}")
    def deposit(self):
        while True:
            try:
                amount = int(input("Enter the amout to deposit: "))
                if amount <= 0:
                    print("You can not deposit unrealistic amount of money ... asshole!")
                else:
                    self.balance += amount
                    return self.balance
            except ValueError:
                print("Enter a valid integer")
            
    def withdraw(self):
        while True:
            try:
                amount = int(input("Enter the amout to withdraw: "))
                if amount > self.balance:
                    print("Amount exceeds available balance")
                elif amount <= 0:
                    print("You can not withdraw unrealistic amount of money ... asshole!")
                else:
                    self.balance -= amount
                    return self.balance
            except ValueError:
                print("Enter a valid integer")
            

obj = BankAccount()
obj.info()
obj.deposit()
obj.withdraw()

obj.info()
