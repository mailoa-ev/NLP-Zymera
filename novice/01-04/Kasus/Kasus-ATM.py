user_id = 0
loop = "n"
users = [
    {
        "id": "1234",
        "no_rekening": "1234567890",
        "username": "Evangs",
        "pin": "1234",
        "saldo": 100000
    }
]
status_login = False
pakai_atm = "y"


def cek_login(p):
    for user in users:
        if user['pin'] == p:
            return user
    return False


def cek_user(id):
    for i in range(len(users)):
        if users[i]['id'] == str(id):
            return int(i)
    return -1


def cek_rekening(no):
    for i in range(len(users)):
        if str(users[i]['no_rekening']) == str(no):
            return int(i)
    return -1


def simpan_uang(uang):
    index1 = cek_user(user_id)
    if index1 >= 0:
        if users[index1]['saldo'] >= int(uang):
            users[index1]['saldo'] = users[index1]['saldo'] + int(uang)
            print("You just deposit Rp." + str(uang))
            print("Your current balance is Rp.", users[index1]['saldo'])
        else:
            print("Ops Anda salah memasukan nominal!")


def ambil_uang(uang):
    index1 = cek_user(user_id)
    if index1 >= 0:
        if users[index1]['saldo'] >= int(uang):
            users[index1]['saldo'] = users[index1]['saldo'] - int(uang)
            print("You just withdraw Rp." + str(uang))
            print("Your current balance is Rp.", users[index1]['saldo'])
        else:
            print("Ops You do not have sufficient money to withdraw!")
            print("Checked your balance to see your money in the bank.")


while pakai_atm == "y":
    while not status_login:
        print("===================================================")
        print("\tWelcome to this simple ATM machine")
        print("===================================================")
        pin = input("Insert PIN : ")

        cl = cek_login(pin)
        if cl:
            print("Welcome " + cl['username'])
            user_id = cl['id']
            status_login = True
            loop = "y"
        else:
            print("")
            print("Ops wrong PIN!")
            print("")
            print("")

    while loop == "y" and status_login:
        u = users[cek_user(user_id)]

        print("Please select ATM Transactions")
        print("1.Deposit")
        print("2.Withdraw")
        print("3.Balance Inquiry")
        print("4.Exit")

        a = int(input("Choose : "))
        if a == 1:
            print("")
            nominal = input("Enter the amount of money to deposit : ")
            simpan_uang(nominal)
            print("")
            loop = "n"
        elif a == 2:
            print("")
            nominal = input("Enter amount of money to withdraw : ")
            ambil_uang(nominal)
            print("")
            loop = "n"
        elif a == 3:
            print("")
            print("Your current balance is Rp.", u['saldo'])
            print("")
            print("")
            loop = "n"
        elif a == 4:
            print("")
            print("Thank you for using this simple ATM Machine.")
            status_login = False
            loop = "n"
            pakai_atm = "n"
        else:
            print("Wrong Input! Please enter a number only (1-4).")
        if status_login == True:
            input("Back to MENU UTAMA (Enter) ")
            print("")
            loop = "y"
