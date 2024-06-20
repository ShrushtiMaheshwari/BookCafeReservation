Customer
- cust_id
- name
- age

Table
- table_id
- capacity
- status

Reservation
- reservation_id
- table_id
- customer_id
- num_customers
- start_time
- end_time

Restaurant
- tables
- opening_time
- closing_time
- reservations

- make_reservation(customer)
- cancel_reservation(reservation)
- update_after_completed_reservation(reservation)
