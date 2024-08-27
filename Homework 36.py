from threading import Thread, Lock

lock = Lock()


class BankAccount:
    def __init__(self, balance):
        self.balance = balance

    def deposit(self, amount):
        lock.acquire()
        self.balance += amount
        print(f'Внесено {amount}, новый баланс {self.balance}')
        lock.release()

    def withdraw(self, amount):
        lock.acquire()
        self.balance -= amount
        print(f'Снято {amount}, новый баланс {self.balance}')
        lock.release()


account = BankAccount(1000)


def deposit_task(account, amount):
    for _ in range(5):
        account.deposit(amount)


def withdraw_task(account, amount):
    for _ in range(5):
        account.withdraw(amount)


deposit_thread = Thread(target=deposit_task, args=(account, 100))
withdraw_thread = Thread(target=withdraw_task, args=(account, 150))

deposit_thread.start()
withdraw_thread.start()

deposit_thread.join()
withdraw_thread.join()
