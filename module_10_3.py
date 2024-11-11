import threading
from random import randint
import time

class Bank:
    def __init__(self):
        self.balance = 0
        self.lock = threading.Lock()

    def deposit(self):
        for _ in range(100):
            amount = randint(50, 500)
            with self.lock:
                self.balance += amount
                print(f"Пополнение: {amount}. Баланс: {self.balance}")
            time.sleep(0.001)

    def take(self):
        for _ in range(100):
            amount = randint(50, 500)
            print(f"Запрос на снятие: {amount}")
            with self.lock:
                if amount > self.balance:
                    print("Запрос отклонён, недостаточно средств")
                    continue
                self.balance -= amount
                print(f"Снятие: {amount}. Баланс: {self.balance}")

bank = Bank()

thread_deposit = threading.Thread(target=bank.deposit)
thread_take = threading.Thread(target=bank.take)

thread_deposit.start()
thread_take.start()

thread_deposit.join()
thread_take.join()

print(f"Итоговый баланс: {bank.balance}")
