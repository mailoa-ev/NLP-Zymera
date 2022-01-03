# ini merupakan jawaban dari kasus yang diberikan saat pertemuan 4

class Deposit:

    balance = 0.00

    def __init__(self, amount):
        self.balance = amount

    def deposit(self, amount):
        self.balance = self.balance + float(amount)

    def withdraw(self, amount):
        self.balance = self.balance - float(amount)

    def get_balance(self):
        return self.balance


if __name__ == "__main__":

    depo = Deposit(0)

    while True:
        print("Welcome to this simple ATM Machine")
        print()
        print("Please select ATM transaction!")
        print("[1] Deposit")
        print("[2] Withdraw")
        print("[3] Balance Inquiry")
        print("[4] Exit")

        action = input("What would you like to do? ")

        if action == "1":
            amount = input("Amount to be saved: ")
            depo.deposit(amount)
        elif action == "2":
            amount = input("Amount to be withdrawn: ")
            depo.withdraw(amount)
        elif action == "3":
            print(depo.get_balance())
        else:
            break
