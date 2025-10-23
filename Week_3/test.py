#establish a class 
class Iteration:
    # Sets up an empty array with a maximum of 100 elements
    def __init__(self):
        self.array = [12,5,19,3,14,9,7,18,2]

#question 1 insertion sort 
    def insertion_sort_arr(self):
            for i in range(1, len(self.array)):
                current_value = self.array[i]
                x = i
                while x > 0 and self.array[x - 1] < current_value:
                    self.array[x] = self.array[x - 1]
                    x -= 1
                self.array[x] = current_value
            return self.array
    
#question 2 binary search 
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
                print("next smallest element is: ", self.array[mid + 1])
                return mid + 1 
        print("Not found")
        return -1
    
    def next_smallest(self):

        for i in range(len(self.array) - 1):
            for x in range(len(self.array) - 1):
                if self.array[x] < self.array[x+1]:
                    return 1 

    

def main():
    itt = Iteration()

    while True: 
        print("--- SELECT OPTION ---")
        print("1 - Insertion Sort")
        print("2 - Binary Search")
        choice = input("Select a choice: ")

        if choice == '1':
            print("After the insertion sort, the array is", itt.insertion_sort_arr())

        elif choice == '2':
            print("the array is: ", itt.insertion_sort_arr())
            target = int(input("Enter target value: "))
            print("Binary search result:", itt.binary_search_arr(target))
            


main()