# Node class for storing data and link
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


# Singly Linked List with CRUD + advanced operations
class SinglyLinkedList:
    def __init__(self):
        self.head = None

    # INSERT a new node at the end
    def insert(self, data):
        new_node = Node(data)

        if not self.head:  # Empty list
            self.head = new_node
            return

        current = self.head
        while current.next:  # Move to last node
            current = current.next
        current.next = new_node

    # SEARCH for a value, return True/False
    def search(self, data):
        current = self.head
        while current:
            if current.data == data:
                return True
            current = current.next
        return False

    # DELETE first occurrence of given value
    def delete(self, data):
        if not self.head:
            return

        # Delete head node
        if self.head.data == data:
            self.head = self.head.next
            return

        current = self.head
        while current.next:
            if current.next.data == data:
                current.next = current.next.next
                return
            current = current.next

    # TRAVERSE and print all nodes
    def traverse(self):
        current = self.head
        if not current:
            print("List is empty.")
            return

        while current:
            print(current.data, end=" -> ")
            current = current.next
        print("None")

    # SWAP data between two nodes
    def swap_nodes(self, a, b):
        temp = a.data
        a.data = b.data
        b.data = temp

    # BUBBLE SORT linked list
    def bubble_sort(self):
        if self.head is None:
            return

        swapped = True
        while swapped:
            swapped = False
            curr = self.head

            while curr.next:
                if curr.data > curr.next.data:
                    self.swap_nodes(curr, curr.next)
                    swapped = True
                curr = curr.next

    # REVERSE linked list
    def reverse(self):
        prev = None
        current = self.head

        while current:
            next_node = current.next
            current.next = prev
            prev = current
            current = next_node

        self.head = prev

    # REMOVE Nth node from the end
    def remove_nth_from_end(self, n):
        dummy = Node(0)
        dummy.next = self.head

        first = dummy
        second = dummy

        for _ in range(n + 1):
            if first is None:
                return
            first = first.next

        while first:
            first = first.next
            second = second.next

        second.next = second.next.next
        self.head = dummy.next

    # MERGE TWO sorted lists into new sorted list
    def merge_two(self, ll1, ll2):
        ll3 = SinglyLinkedList()
        n1 = ll1.head
        n2 = ll2.head

        while n1 and n2:
            if n1.data < n2.data:
                ll3.insert(n1.data)
                n1 = n1.next
            else:
                ll3.insert(n2.data)
                n2 = n2.next

        while n1:
            ll3.insert(n1.data)
            n1 = n1.next

        while n2:
            ll3.insert(n2.data)
            n2 = n2.next

        return ll3

    # MERGE N sorted lists using repeated merging
    def merge_n(self, list_of_lists):
        if not list_of_lists:
            return None

        result = list_of_lists[0]

        for i in range(1, len(list_of_lists)):
            result = self.merge_two(result, list_of_lists[i])

        return result



def menu():
    sll = SinglyLinkedList()

    while True:
        print("\n=========== Linked List Menu ===========")
        print("1. Insert element")
        print("2. Search element")
        print("3. Delete element")
        print("4. Traverse list (Print list)")
        print("5. Sort list (Bubble Sort)")
        print("6. Reverse list")
        print("7. Remove N-th node from end")
        print("8. Merge TWO sorted lists")
        print("9. Merge N sorted lists")
        print("0. Exit")
        print("========================================")

        choice = input("Enter choice: ")

        # INSERT
        if choice == "1":
            val = int(input("Enter value to insert: "))
            sll.insert(val)
            print("Inserted.")

        # SEARCH
        elif choice == "2":
            val = int(input("Enter value to search: "))
            print("Found!" if sll.search(val) else "Not found.")

        # DELETE
        elif choice == "3":
            val = int(input("Enter value to delete: "))
            sll.delete(val)
            print("Deleted (if existed).")

        # TRAVERSE
        elif choice == "4":
            print("Linked List:")
            sll.traverse()

        # SORT
        elif choice == "5":
            sll.bubble_sort()
            print("List sorted.")

        # REVERSE
        elif choice == "6":
            sll.reverse()
            print("List reversed.")

        # REMOVE N-th from end
        elif choice == "7":
            n = int(input("Enter N: "))
            sll.remove_nth_from_end(n)
            print("Node removed (if existed).")

        # MERGE TWO SORTED LISTS
        elif choice == "8":
            print("\n-- Enter elements for List 1 (comma separated) --")
            l1_values = list(map(int, input().split(',')))
            list1 = SinglyLinkedList()
            for v in l1_values:
                list1.insert(v)
            list1.bubble_sort()

            print("\n-- Enter elements for List 2 (comma separated) --")
            l2_values = list(map(int, input().split(',')))
            list2 = SinglyLinkedList()
            for v in l2_values:
                list2.insert(v)
            list2.bubble_sort()

            merged = sll.merge_two(list1, list2)
            print("\nMerged List:")
            merged.traverse()

        # MERGE N LISTS
        elif choice == "9":
            count = int(input("How many lists? "))
            lists = []

            for i in range(count):
                vals = list(map(int, input(f"Enter elements for List {i+1}: ").split(',')))
                temp = SinglyLinkedList()
                for v in vals:
                    temp.insert(v)
                temp.bubble_sort()
                lists.append(temp)

            merged = sll.merge_n(lists)
            print("\nMerged List:")
            merged.traverse()

        # EXIT
        elif choice == "0":
            print("Exiting...")
            break

        else:
            print("Invalid choice! Try again.")


# Run the menu
menu()
