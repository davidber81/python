import threading

class BankAccount:
    def __init__(self, account, amount):
        self.account = account
        self.amount = amount
        self.lock = threading.Lock()

    def deposit(self, amount):
        with self.lock:
            print(f"Внесли сумму {amount} на счету {account.amount}")
            self.amount += amount

    def withdraw(self, amount):
        with self.lock:
            if self.amount >= amount:
                print(f"Сняли сумму {amount} на счету {account.amount} ")
                self.amount -= amount
            else:
                print("Not enough funds to withdraw")

def deposit_task(account, amount):
    for _ in range(5):
        account.deposit(amount)

def withdraw_task(account, amount):
    for _ in range(5):
        account.withdraw(amount)

account = BankAccount('100', 500)

print("Начальный баланс счета", account.amount)

deposit_thread = threading.Thread(target=deposit_task, args=(account, 100))
withdraw_thread = threading.Thread(target=withdraw_task, args=(account, 150))

deposit_thread.start()
withdraw_thread.start()

deposit_thread.join()
withdraw_thread.join()

print("Итоговый баланс счета", account.amount)