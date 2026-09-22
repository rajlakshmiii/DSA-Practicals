
class Node:
    def __init__(self, roll_no, name, marks):
        self.roll_no = roll_no
        self.name = name
        self.marks = marks
        self.next = None

class StudentRecordSystem:
    def __init__(self):
        self.head = None

    def add_student(self):
        roll_no = int(input("Enter Roll No: "))
        name = input("Enter Student Name: ")
        marks = float(input("Enter Marks: "))

        new_node = Node(roll_no, name, marks)

        if self.head is None:
            self.head = new_node
        else:
            temp = self.head

            while temp.next is not None:
                temp = temp.next

            temp.next = new_node

        print("Student record added successfully.")

    def delete_student(self):
        if self.head is None:
            print("List is empty.")
            return

        roll_no = int(input("Enter Roll No to delete: "))

        if self.head.roll_no == roll_no:
            self.head = self.head.next
            print("Student record deleted successfully.")
            return

        temp = self.head

        while temp.next is not None:
            if temp.next.roll_no == roll_no:
                temp.next = temp.next.next
                print("Student record deleted successfully.")
                return

            temp = temp.next

        print("Student record not found.")

    def update_student(self):
        if self.head is None:
            print("List is empty.")
            return

        roll_no = int(input("Enter Roll No to update: "))

        temp = self.head

        while temp is not None:
            if temp.roll_no == roll_no:
                print("Current Name:", temp.name)
                print("Current Marks:", temp.marks)

                temp.name = input("Enter New Name: ")
                temp.marks = float(input("Enter New Marks: "))

                print("Student record updated successfully.")
                return

            temp = temp.next

        print("Student record not found.")

    def search_student(self):
        if self.head is None:
            print("List is empty.")
            return

        roll_no = int(input("Enter Roll No to search: "))

        temp = self.head

        while temp is not None:
            if temp.roll_no == roll_no:
                print("\nStudent Found")
                print("Roll No :", temp.roll_no)
                print("Name    :", temp.name)
                print("Marks   :", temp.marks)
                return

            temp = temp.next

        print("Student record not found.")

    def sort_students(self):
        if self.head is None or self.head.next is None:
            print("List is already sorted.")
            return

        current = self.head

        while current is not None:
            index = current.next

            while index is not None:
                if current.marks > index.marks:

                    current.roll_no, index.roll_no = (
                        index.roll_no,
                        current.roll_no
                    )

                    current.name, index.name = (
                        index.name,
                        current.name
                    )

                    current.marks, index.marks = (
                        index.marks,
                        current.marks
                    )

                index = index.next

            current = current.next

        print("Student records sorted by marks successfully.")

    def display_students(self):
        if self.head is None:
            print("List is empty.")
            return

        temp = self.head

        print("\n---------------------------------------")
        print("       STUDENT RECORDS")
        print("---------------------------------------")
        print("Roll No\tName\t\tMarks")
        print("---------------------------------------")

        while temp is not None:
            print(f"{temp.roll_no}\t{temp.name:<15}\t{temp.marks}")
            temp = temp.next

        print("---------------------------------------")

student_system = StudentRecordSystem()

while True:

    print("\n======================================")
    print(" STUDENT RECORD MANAGEMENT SYSTEM")
    print("======================================")
    print("1. Add Student")
    print("2. Delete Student")
    print("3. Update Student")
    print("4. Search Student")
    print("5. Sort Students")
    print("6. Display Students")
    print("7. Exit")
    print("======================================")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        student_system.add_student()

    elif choice == 2:
        student_system.delete_student()

    elif choice == 3:
        student_system.update_student()

    elif choice == 4:
        student_system.search_student()

    elif choice == 5:
        student_system.sort_students()

    elif choice == 6:
        student_system.display_students()

    elif choice == 7:
        print("Program terminated.")
        break

    else:
        print("Invalid choice. Please try again.")
