# Define a node for the singly linked list
class Node:
    def __init__(self, data):
        # store the value and a reference to the next node
        self.data = data
        self.next = None


# Define the singly linked list (SLL) class with basic operations
class SLL:
    def __init__(self):
        # head points to the first node in the list
        self.head = None

    def insert(self, data):
        """Insert a new node with `data` at the end of the list."""
        new_node = Node(data)

        # if list is empty, new node becomes the head
        if not self.head:
            self.head = new_node
            return

        # otherwise walk to the end and append
        current = self.head
        while current.next:
            current = current.next
        current.next = new_node

    def search(self, data):
        """Return True if a node with `data` exists in the list, else False."""
        current = self.head
        while current:
            if current.data == data:
                return True
            current = current.next
        return False

    def delete(self, data):
        """Delete the first node that contains `data`. If not found, do nothing."""
        # nothing to delete
        if not self.head:
            return

        # if the head contains the data, remove it
        if self.head.data == data:
            self.head = self.head.next
            return

        # search for the node whose next node contains the data
        current = self.head
        while current.next:
            if current.next.data == data:
                # bypass the node to delete it
                current.next = current.next.next
                return
            current = current.next

    def traverse(self):
        """Print all node values in order."""
        current = self.head
        while current:
            print(current.data)
            current = current.next


def _parse_input_value(user_input):
    """Try to convert input to int, otherwise return the original string."""
    try:
        return int(user_input)
    except ValueError:
        return user_input


def menu():
    """Interactive multiple-choice menu to operate on the linked list."""
    sll = SLL()

    # pre-populate with a few values for demonstration
    sll.insert(10)
    sll.insert(20)
    sll.insert(30)

    while True:
        print('\nChoose an action:')
        print('1) Insert a value')
        print('2) Delete a value')
        print('3) Search for a value')
        print('4) Traverse / print the list')
        print('5) Show example operations (re-populate demo list)')
        print('6) Exit')

        choice = input('Enter choice (1-6): ').strip()

        if choice == '1':
            val = _parse_input_value(input('Enter value to insert: ').strip())
            sll.insert(val)
            print('Inserted:', val)

        elif choice == '2':
            val = _parse_input_value(input('Enter value to delete: ').strip())
            sll.delete(val)
            print('Attempted delete of:', val)

        elif choice == '3':
            val = _parse_input_value(input('Enter value to search for: ').strip())
            found = sll.search(val)
            print('Found' if found else 'Not found')

        elif choice == '4':
            print('\nList contents:')
            sll.traverse()

        elif choice == '5':
            # clear and re-populate demo list
            sll = SLL()
            sll.insert(10)
            sll.insert(20)
            sll.insert(30)
            print('Demo list re-populated with 10, 20, 30')

        elif choice == '6':
            print('Exiting.')
            break

        else:
            print('Invalid choice, please enter a number between 1 and 6.')


def main():
    # run the interactive menu when executed directly
    menu()


if __name__ == '__main__':
    main()