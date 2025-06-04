from dataclasses import dataclass
from mysql.connector import Date

@dataclass
class Order:
    order_id:int
    customer_id: int
    order_status: int
    order_date: Date
    required_date: Date
    shipped_date: Date
    store_id: int
    staff_id: int

    def __hash__(self):
        return hash(self.order_id)

    def __eq__(self, other):
        return self.order_id == other.order_id

    def __str__(self):
        return self.order_id