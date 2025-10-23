# This program demonstrates different ways to sort and search through a list of numbers.
# It uses a class called Iteration to group multiple sorting and searching algorithms
# and lets the user test them through a simple menu interface.

from random import sample  # Used to create a random list of numbers

class Iteration:
    # Sets up an empty array with a maximum of 100 elements
    def __init__(self):
        self.array = []
        self.max_size = 100 

    # Fills the array with 100 unique random numbers between 1 and 300
    def fill_arr(self):
        self.array = sample(range(1, 3 * self.max_size), self.max_size)

    # Prints the array and its length
    def print_arr(self):
        print("The length of the array in total is ", len(self.array))
        print("The contents of the array are\n", self.array)

    # === SELECTION SORT ===
    # Finds the smallest element and swaps it to the correct position each time.
    #
    # HOW IT WORKS:
    # - Repeatedly selects the smallest unsorted value and moves it to the front.
    # WHY IT WORKS:
    # - Each step places one element in its final, correct position.
    #
    # EXAMPLE:
    # [5, 2, 4, 1]
    # Step 1: Find smallest (1) → swap with first → [1, 2, 4, 5]
    # Step 2: Remaining [2, 4, 5] → already sorted → DONE
    def sort_arr(self):
        for i in range(len(self.array) - 1):
            minimum = i
            for x in range(i + 1, len(self.array)):
                if self.array[x] < self.array[minimum]:
                    minimum = x
            self.array[minimum], self.array[i] = self.array[i], self.array[minimum]
        return self.array

    # === INSERTION SORT ===
    # Builds the sorted list one element at a time by inserting items in order.
    #
    # HOW IT WORKS:
    # - Takes the next element and shifts larger ones to the right until the correct spot is found.
    # WHY IT WORKS:
    # - The left side of the array remains sorted at all times.
    #
    # EXAMPLE:
    # [5, 3, 4]
    # Step 1: Compare 3 with 5 → insert before → [3, 5, 4]
    # Step 2: Compare 4 → insert between 3 and 5 → [3, 4, 5]
    def insertion_sort_arr(self):
        for i in range(1, len(self.array)):
            current_value = self.array[i]
            x = i
            while x > 0 and self.array[x - 1] > current_value:
                self.array[x] = self.array[x - 1]
                x -= 1
            self.array[x] = current_value
        return self.array

    # === BUBBLE SORT ===
    # Repeatedly compares neighbouring items and swaps them if they are in the wrong order.
    #
    # HOW IT WORKS:
    # - Each pass "bubbles up" the largest value to the end.
    # WHY IT WORKS:
    # - Small values move down the list, large values rise up like bubbles.
    #
    # EXAMPLE:
    # [4, 3, 1]
    # Pass 1: Compare 4>3 → swap → [3, 4, 1]; then 4>1 → swap → [3, 1, 4]
    # Pass 2: Compare 3>1 → swap → [1, 3, 4]
    def bubble_Sort_arr(self):
        for i in range(len(self.array) - 1):
            for x in range(len(self.array) - 1):
                if self.array[x] > self.array[x + 1]:
                    self.array[x], self.array[x + 1] = self.array[x + 1], self.array[x]
        return self.array

    # === LINEAR SEARCH ===
    # Checks each element in the list one by one until the target is found.
    #
    # HOW IT WORKS:
    # - Starts from the beginning and stops when a match is found.
    # WHY IT WORKS:
    # - It directly compares every value with the target.
    #
    # EXAMPLE:
    # List = [5, 8, 2, 9], Target = 2
    # Checks 5 (no), 8 (no), 2 (yes) → Found at index 2
    def linear_arr(self, target):
        for i in range(len(self.array)):
            if self.array[i] == target:
                return i
        print("Nothing located matching your target")
        return -1

    # === BINARY SEARCH ===
    # A fast search that only works on a sorted list.
    #
    # HOW IT WORKS:
    # - Looks at the middle value and decides if the target is left or right.
    # - Repeats this until the value is found or the range is empty.
    # WHY IT WORKS:
    # - Each comparison removes half of the remaining data, making it very efficient.
    #
    # EXAMPLE:
    # Sorted list = [1, 3, 5, 7, 9], Target = 7
    # Step 1: mid = 5 (index 2) → 7 > 5 → search right
    # Step 2: mid = 7 (index 3) → FOUND
    def binary_search_arr(self, target):
        start = 0
        end = len(self.array) - 1
        while start <= end:
            mid = (start + end) // 2
            if self.array[mid] < target:
                start = mid + 1
            elif self.array[mid] > target:
                end = mid - 1
            else:
                return mid
        print("Not found")
        return -1

    # === RECURSIVE BINARY SEARCH ===
    # Works the same way as binary search but uses recursion.
    #
    # HOW IT WORKS:
    # - The function calls itself to search smaller halves of the list.
    # WHY IT WORKS:
    # - It divides the search space in half each time until the item is found.
    #
    # EXAMPLE:
    # [2, 4, 6, 8, 10], Target = 4
    # mid = 6 → 4 < 6 → search left half [2, 4]
    # mid = 4 → FOUND
    def binaryRecurSearch(self, item):
        return self._binaryRecurSearch(self.array, 0, len(self.array) - 1, item)

    def _binaryRecurSearch(self, arr, start, end, item):
        if start <= end:
            mid = (start + end) // 2
            if arr[mid] < item:
                return self._binaryRecurSearch(arr, mid + 1, end, item)
            elif arr[mid] > item:
                return self._binaryRecurSearch(arr, start, mid - 1, item)
            else:
                return mid
        print("Not found")
        return -1

    # === TERNARY SEARCH ===
    # Similar to binary search, but splits the list into three parts instead of two.
    #
    # HOW IT WORKS:
    # - Calculates two midpoints.
    # - Determines which of the three parts might contain the target.
    # WHY IT WORKS:
    # - Reduces the search range by one-third each time, using the same divide-and-conquer idea.
    #
    # EXAMPLE:
    # [1, 3, 5, 7, 9, 11], Target = 9
    # mid1 = 3, mid2 = 7 → 9 > 7 → search right section [9, 11]
    # mid = 9 → FOUND
    def ternarySearch(self, item):
        return self._ternarySearch(self.array, 0, len(self.array) - 1, item)
    
    def _ternarySearch(self, arr, start, end, item):
        if start <= end:
            third1 = start + (end - start) // 3
            third2 = end - (end - start) // 3

            if arr[third1] == item:
                return third1
            elif arr[third2] == item:
                return third2
            if item < arr[third1]:
                return self._ternarySearch(arr, start, third1 - 1, item)
            elif item > arr[third2]:
                return self._ternarySearch(arr, third2 + 1, end, item)
            else:
                return self._ternarySearch(arr, third1 + 1, third2 - 1, item)

        print("Not found")
        return -1

# Displays a simple menu for choosing operations
def display_menu():
    print("\n=== Sorting and Searching Menu ===")
    print("1. Fill, Sort, and Print Array (Selection Sort)")
    print("2. Fill, Print Array, then Bubble Sort")
    print("3. Fill, Linear Search, then Insertion Sort")
    print("4. Fill, Bubble Sort, Linear & Binary Search")
    print("5. Fill, Bubble Sort, Binary & Recursive Binary Search")
    print("6. Fill, Bubble Sort, All Search Methods (Linear, Binary, Binary Rec, Ternary)")
    print("0. Exit")

# The main function — lets the user choose and test algorithms
def main():
    queue = Iteration()  # Create an Iteration object

    while True:
        display_menu()
        choice = input("Enter your choice: ")

        if choice == '1':
            queue.fill_arr()
            queue.sort_arr()
            queue.print_arr()

        elif choice == '2':
            queue.fill_arr()
            queue.print_arr()
            print("After the bubble sort, the array is", queue.bubble_Sort_arr())

        elif choice == '3':
            queue.fill_arr()
            target = int(input("Enter target value for linear search: "))
            result = queue.linear_arr(target)
            print("Linear search result:", result)
            print("After the insertion sort, the array is", queue.insertion_sort_arr())

        elif choice == '4':
            queue.fill_arr()
            queue.print_arr()
            print("After the bubble sort, the array is", queue.bubble_Sort_arr())
            target = int(input("Enter target value: "))
            print("Linear search result:", queue.linear_arr(target))
            print("Binary search result:", queue.binary_search_arr(target))

        elif choice == '5':
            queue.fill_arr()
            queue.print_arr()
            print("After the bubble sort, the array is", queue.bubble_Sort_arr())
            target = int(input("Enter target value: "))
            print("Binary search result:", queue.binary_search_arr(target))
            print("Recursive binary search result:", queue.binaryRecurSearch(target))

        elif choice == '6':
            queue.fill_arr()
            queue.print_arr()
            print("After the bubble sort, the array is", queue.bubble_Sort_arr())
            target = int(input("Enter target value: "))
            print("Linear search:", queue.linear_arr(target))
            print("Binary search:", queue.binary_search_arr(target))
            print("Recursive binary search:", queue.binaryRecurSearch(target))
            print("Ternary search:", queue.ternarySearch(target))

        elif choice == '0':
            print("Exiting program.")
            break

        else:
            print("Invalid choice. Please try again.")

# Run the main program
if __name__ == "__main__":
    main()
