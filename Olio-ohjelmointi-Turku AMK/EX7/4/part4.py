class Order:
    _id_counter = 1
    
    def __init__(self, description, programmer, workload):
        self._id = Order._id_counter
        Order._id_counter += 1
        self._description = description
        self._programmer = programmer
        self._workload = workload
        self._completed = False
    
    @property
    def id(self):
        return self._id
    
    @property
    def description(self):
        return self._description
    
    @property
    def programmer(self):
        return self._programmer
    
    @property
    def workload(self):
        return self._workload
    
    def is_completed(self):
        return self._completed
    
    def mark_completed(self):
        self._completed = True
    
    def __str__(self):
        status = "COMPLETED" if self._completed else "NOT COMPLETED"
        return f"{self._id}: {self._description} ({self._workload} hours), programmer {self._programmer} {status}"

class OrderBook:
    def __init__(self):
        self._orders = []
    
    def add_order(self, description, programmer, workload):
        order = Order(description, programmer, workload)
        self._orders.append(order)
    
    def all_orders(self):
        return self._orders
    
    def programmers(self):
        return list(set(order.programmer for order in self._orders))
    
    def mark_completed(self, order_id):
        for order in self._orders:
            if order.id == order_id:
                order.mark_completed()
                return True
        raise ValueError(f"No order found with id {order_id}")
    
    def mark_finished(self, order_id):
        self.mark_completed(order_id)
    
    def unfinished_orders(self):
        return [order for order in self._orders if not order.is_completed()]
    
    def finished_orders(self):
        return [order for order in self._orders if order.is_completed()]
    
    def status_of_programmer(self, programmer):
        finished_count = 0
        unfinished_count = 0
        finished_workload = 0
        unfinished_workload = 0
        for order in self._orders:
            if order.programmer == programmer:
                if order.is_completed():
                    finished_count += 1
                    finished_workload += order.workload
                else:
                    unfinished_count += 1
                    unfinished_workload += order.workload
        if finished_count == 0 and unfinished_count == 0:
            raise ValueError(f"No orders found for programmer {programmer}")
        return (finished_count, unfinished_count, finished_workload, unfinished_workload)

# Example usage
order_book = OrderBook()
order_book.add_order("program webstore", "Adele", 10)
order_book.add_order("program mobile app for workload accounting", "Adele", 25)
order_book.add_order("program app for practising mathematics", "Adele", 100)
order_book.add_order("program the next facebook", "Eric", 1000)

order_book.mark_finished(1)
order_book.mark_finished(2)

status = order_book.status_of_programmer("Adele")
print(status)