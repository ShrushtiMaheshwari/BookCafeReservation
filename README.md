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
- cust_id
- num_customers
- start_time
- end_time

Restaurant
- tables
- start_time
- end_time
- reservation_mgmt_system

ReservationManagementSystem
- reservations

- make_reservation(customer, num_customers)
- cancel_reservation(reservation)
- update_after_completed_reservation(reservation)
