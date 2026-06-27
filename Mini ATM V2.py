print("WELCOME TO MINI ATM MACHINE")
account_name = "arohi"
pin = "1234"
balance = 5000
attempts = 3
history = []
def check_balance():
    print("your current balance:", balance)
def deposit():
    global balance
    amount = int(input("enter amount to deposit: "))
    if amount <= 0:
        print("invalid amount")
        return
    balance += amount
    history.append(f"deposit {amount}")
    print("money added successfullly")
    print("new balance", balance)
def withdraw():
    global balance
    amount = int(input("enter amount to withdraw: "))
    if amount <= 0:
        print("invalid amount")
        return
    if amount <= balance:
        balance -= amount
        history.append(f"withdraw {amount}")
        print("money withdrawn successfully")
        print("remaining balance", balance)
    else:
        print("insifficient balance")
def change_pin():
    global pin
    old_pin = input("enter old pin: ")
    if old_pin == pin:
        new_pin = input("enter new pin: ")
        pin = new_pin
        history.append("pin changed")
        print("pin changes successfully")
    else:
        print("wrong old pin")
def show_details():
    print("===========ACCOUNT DETAILS============")
    print("account name-", account_name)
    print("balance-", balance)
    print("pin - ****")
def show_history():
    print("========= TRANSACTION HISTORY ==========")
    if len(history) == 0:
        print("no transaction yet")
    else:
        for i, item in enumerate(history, start=1):
            print(f"{i}. {item}")
while attempts > 0:
    entered_pin = input("enter pin: ")
    if entered_pin == pin:
        print("login successful")
        break
    else:
        print("wrong pin")
        attempts -= 1
        print("attempts left", attempts)
        if attempts == 0:
            print("account locked")
            exit()
while True:
    print("--------------MENU----------------")
    print("1. check balance")
    print("2. deposit money")
    print("3. withdraw money")
    print("4. change pin")
    print("5. check details")
    print("6. transaction history")
    print("7. exit")
    print("==============================")
    choice = int(input("choose any option: "))
    if choice == 1:
        check_balance()
    elif choice == 2:
        deposit()
    elif choice == 3:
        withdraw()
    elif choice == 4:
        change_pin()
    elif choice == 5:
        show_details()
    elif choice == 6:
        show_history()
    elif choice == 7:
        print("thank youu for using atm")
        break
    else:
        print("invalid option")
            