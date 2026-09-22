
undo_stack = []
redo_stack = []

document = ""


def make_change(new_text):
    global document

    undo_stack.append(document)

    document = new_text

    redo_stack.clear()

    print("\nChange applied successfully.")

def undo():
    global document

    if not undo_stack:
        print("\nNothing to Undo.")
        return

    redo_stack.append(document)

    document = undo_stack.pop()

    print("\nUndo successful.")

def redo():
    global document

    if not redo_stack:
        print("\nNothing to Redo.")
        return

    undo_stack.append(document)

    document = redo_stack.pop()

    print("\nRedo successful.")

def display_document():
    print("\nCurrent Document State:")
    print(document)


while True:

    print("\n========== TEXT EDITOR ==========")
    print("1. Make a Change")
    print("2. Undo")
    print("3. Redo")
    print("4. Display Document State")
    print("5. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        new_text = input("Enter new document text: ")
        make_change(new_text)

    elif choice == "2":
        undo()

    elif choice == "3":
        redo()

    elif choice == "4":
        display_document()

    elif choice == "5":
        print("\nExiting the application...")
        break

    else:
        print("\nInvalid choice. Please try again.")