import threading
import time
from queue import Queue

class Table:
    def __init__(self, number):
        self.number = number
        self.is_busy = False
class Customer(threading.Thread):
    def __init__(self, number, table):
        super().__init__()
        self.number = number
        self.table = table

    def run(self):
        print(f"Посетитель номер {self.number} прибыл")
        while self.table.is_busy:
            time.sleep(1)
        self.table.is_busy = True
        print(f"Посетитель номер {self.number} сел за стол {self.table.number} (начало обслуживания)")
        time.sleep(5)
        print(f"Посетитель номер {self.number} покушал и ушёл (конец обслуживания)")
        self.table.is_busy = False
class Cafe:
    def __init__(self, tables):
        self.tables = tables
        self.queue = Queue()

    def customer_arrival(self):
        customer_number = 1
        while customer_number <= 20:
            time.sleep(1)
            free_table = None
            for table in self.tables:
                if not table.is_busy:
                    free_table = table
                    break
            if free_table:
                customer_thread = Customer(customer_number, free_table)
                customer_thread.start()
                customer_number += 1
            else:
                print(f"Посетитель номер {customer_number} ожидает свободный стол (помещение в очередь)")
                self.queue.put(customer_number)
                customer_number += 1

table1 = Table(1)
table2 = Table(2)
table3 = Table(3)
tables = [table1, table2, table3]

cafe = Cafe(tables)

customer_arrival_thread = threading.Thread(target=cafe.customer_arrival)
customer_arrival_thread.start()

customer_arrival_thread.join()