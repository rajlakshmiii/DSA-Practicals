
from collections import deque

call_queue = deque()

def add_call(customer_id, call_time):
    call = (customer_id, call_time)
    call_queue.append(call)

    print("\nCall added successfully.")
    print("Customer ID:", customer_id)
    print("Call Time:", call_time, "minutes")

def answer_call():
    if not call_queue:
        print("\nNo calls waiting.")
        return

    customer_id, call_time = call_queue.popleft()

    print("\nCall answered successfully.")
    print("Customer ID:", customer_id)
    print("Call Time:", call_time, "minutes")

def view_queue():
    if not call_queue:
        print("\nQueue is empty.")
        return

    print("\nCurrent Call Queue:")

    for customer_id, call_time in call_queue:
        print("Customer ID:", customer_id, "| Call Time:", call_time, "minutes")

def is_queue_empty():
    if not call_queue:
        print("\nQueue is empty.")
    else:
        print("\nQueue is not empty.")

while True:

    print("\n========== CALL CENTER ==========")
    print("1. Add Call")
    print("2. Answer Call")
    print("3. View Queue")
    print("4. Check Queue Empty")
    print("5. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        customer_id = int(input("Enter Customer ID: "))
        call_time = float(input("Enter Call Time (in minutes): "))

        add_call(customer_id, call_time)

    elif choice == "2":
        answer_call()

    elif choice == "3":
        view_queue()

    elif choice == "4":
        is_queue_empty()

    elif choice == "5":
        print("\nExiting Call Center Simulation...")
        break

    else:
        print("\nInvalid choice. Please try again.")
