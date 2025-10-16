# This program demonstrates different ways to sort and search through a list of numbers.
# It uses a class called Iteration to keep everything organised.

from random import sample  # Used to create a random list of numbers

class Iteration:
    # This sets up the class with an empty list and a maximum size of 100
    def __init__(self):
        self.array = []
        self.max_size = 100 

    # This fills the list with 100 unique random numbers
    def fill_arr(self):
        self.array = sample(range(1, 3 * self.max_size), self.max_size)

    # This prints out the length and contents of the list
    def print_arr(self):
        print("The length of the array in total is ", len(self.array))
        print("The contetents of the array before sorting are\n", self.array)

    # This sorts the list using the selection sort method
    def sort_arr(self):
        for i in range (len(self.array) - 1): # Go through each item
            minimum = i 
            for x in range(i + 1, len(self.array)):
                # Find the smallest item in the unsorted part
                if (self.array[x] < self.array[minimum]):
                    minimum = x
            # Swap the smallest item with the current position
            self.array[minimum], self.array[i] = self.array[i], self.array[minimum]
        return self.array
            

    # This sorts the list using the insertion sort method
    def insertion_sort_arr(self):
        for i in range (1, len(self.array) - 1):
            current_value = self.array[i]
            x = i 
            # Move the current value to its correct position in the sorted part
            while (x > 0 and current_value < self.array[x -1]): 
                x -= 1
            self.array[x] = current_value
        return self.array
    

    # This sorts the list using the bubble sort method
    def bubble_Sort_arr(self):
        for i in range (len(self.array)-1 ):
            for x in range (len(self.array) -1):
                # Compare each pair of items and swap if needed
                if (self.array[x] > self.array[x + 1]):
                    self.array[x], self.array[x + 1] = self.array[x + 1], self.array[x]
        return self.array

    # This searches for a value by looking at each item one by one
    def linear_arr(self, target): # target is the number to find
        for i in range (len(self.array)):
            if (self.array[i] == target):
                return i  # Return the position if found
        print("Nothing located matching your target")
        return -1  # Return -1 if not found
    
    # This searches for a value using binary search (must be sorted first)
    def binary_search_arr(self, target):
        start = 0
        end = len(self.array) - 1
        while (start <= end):
            mid = (start + end) // 2
            if (self.array[mid] < target):
                start = mid + 1
            elif (self.array[mid] > target):
                end = mid - 1
            else:
                return mid  # Found the target
        print("Not found")
        return -1  # Not found
    

    # This does binary search using recursion (calls itself)
    def binaryRecurSearch(self, item):
        return self._binaryRecurSearch(self.array, 0, len(self.array) - 1, item)

    def _binaryRecurSearch(self, arr, start, end, item):
        # If the search space is valid
        if (start <= end):
            mid = (start + end) // 2
            if (arr[mid] < item):
                return self._binaryRecurSearch(arr, mid + 1, end, item)
            elif (arr[mid] > item):
                return self._binaryRecurSearch(arr, start, mid - 1, item)
            else:
                return mid  # Found the item
        print("Not found")
        return -1  # Not found

    # This searches for a value using ternary search (splits into three parts)
    def ternarySearch(self, item):
        return self._ternarySearch(self.array, 0, len(self.array) - 1, item)
    
    def _ternarySearch(self, arr, start, end, item):
        # If the search space is valid
        if (start <= end):
            third1 = (end - start) // 3 + start
            if (arr[third1] == item):
                return third1
            elif (arr[third1] > item):
                return self._ternarySearch(arr, start, third1 - 1, item)
            else:
                third2 = (end - start) // 3 + third1
                if (arr[third2] == item):
                    return third2
                elif (arr[third2] > item):
                    return self._ternarySearch(arr, third1 + 1, third2 - 1, item)
                else:
                    return self._ternarySearch(arr, third2 + 1, end, item)
        print("Not found")
        return -1  # Not found

# This function prints out the menu for the user
def display_menu():
    print("\n=== Queue Operations Menu ===")
    print("1. Fill, Sort, and Print Array")
    print("2. Fill, Print Array, then Bubble Sort")
    print("3. Fill, Linear Search, then Insertion Sort")
    print("4. Fill, Bubble Sort, Linear & Binary Search")
    print("5. Fill, Bubble Sort, Binary & Recursive Binary Search")
    print("6. Fill, Bubble Sort, All Search Methods (Linear, Binary, Binary Rec, Ternary)")
    print("0. Exit")

# This is the main part of the program that runs everything
def main():
    queue = Iteration()  # Create an object to use the sorting and searching methods

    while True:
        display_menu()  # Show the menu
        choice = input("Enter your choice: ")  # Get the user's choice

        if choice == '1':
            queue.fill_arr()  # Fill the list with random numbers
            queue.sort_arr()  # Sort the list
            queue.print_arr() # Print the sorted list

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
            print("Position of your target is:", result)

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
            break  # Stop the program

        else:
            print("Invalid choice. Please try again.")

# This runs the main function if the file is run directly
if __name__ == "__main__":
    main()