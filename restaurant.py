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


class Reservation:
    def __init__(self, reservation_id, table_id, cust_id, num_customers, start_time, end_time):
        self._reservation_id = reservation_id
        self._table_id = table_id
        self._cust_id = cust_id
        self._num_customers = num_customers
        self._start_time = start_time
        self._end_time = end_time


class ReservationManagementSystem:
    def __init__(self, reservations):
        self._reservations = reservations

    def make_reservation(self, customer, num_customers):
        pass

    def cancel_reservation(self, reservation):
        pass

    def update_after_completed_reservation(self, reservation):
        pass


class Restaurant:
    def __init__(self, tables, start_time, end_time):
        self._tables = tables
        self._start_time = start_time
        self._end_time = end_time
