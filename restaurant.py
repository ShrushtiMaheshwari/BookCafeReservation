class Customer:
    def __init__(self, cust_id, name, age) -> None:
        self._cust_id = cust_id
        self._name = name
        self._age = age

class Table:
    def __init__(self, table_id, capacity, status) -> None:
        self._table_id = table_id
        self._capacity = capacity
        self._status = status
        