class Queue:

    def __init__(self):
        self.data = []
        self.head = 0
        self.tail = -1
        self.max_size = 20  # increased to handle larger queues safely

    def enqueue(self, newData):
        print("Enqueue the data " + str(newData))
        if self.tail == self.max_size - 1:
            # When the queue is full
            raise OverflowError("Cannot insert into a full queue.")
        self.tail += 1
        self.data.insert(self.tail, newData)
        print("Now the tail index is " + str(self.tail))

    def dequeue(self):
        if self.tail == -1:
            # When the queue is empty
            raise IndexError("Cannot delete from an empty queue.")
        removed = self.data[self.head]
        print("Dequeue the data " + str(removed))
        temp = self.head
        while temp < self.tail:
            temp += 1
            self.data[temp - 1] = self.data[temp]
        del self.data[temp]
        self.tail -= 1
        return removed

    def peek(self):
        if self.tail == -1:
            raise IndexError("Cannot peek from an empty queue.")
        print("Peek the head")
        return self.data[self.head]

    def length(self):
        return self.tail + 1

    def print_message(self):
        print("The queue size is " + str(self.length()) + " The first element is " + str(self.peek()))

    def print_all(self):
        while self.tail != -1:
            print(self.dequeue())

    def reverse(self):
        print("\nBefore reverse, the queue is", self.data)
        stack = Stack()
        # Move all elements from queue to stack
        while self.length() > 0:
            element = self.dequeue()
            stack.push(element)
        # Move all elements back to queue
        while stack.length() > 0:
            element = stack.pop()
            self.enqueue(element)
        print("The reversed queue is", self.data)


class Stack:
    def __init__(self):
        self.data = []
        self.top = -1
        self.max_size = 15

    def push(self, newData):
        print("Push the data " + str(newData))
        if self.top == self.max_size - 1:
            raise OverflowError("Cannot insert into a full stack.")
        self.top += 1
        self.data.insert(self.top, newData)
        print("Now the top index is", str(self.top))

    def pop(self):
        if self.top == -1:
            raise IndexError("Cannot delete from an empty stack.")
        removed = self.data[self.top]
        del self.data[self.top]
        self.top -= 1
        print("Pop the data " + str(removed))
        return removed

    def peek(self):
        if self.top == -1:
            raise IndexError("Cannot peek from an empty stack.")
        print("Peek the top")
        return self.data[self.top]

    def length(self):
        return self.top + 1

    def print_message(self):
        print("The stack size is " + str(self.length()) +
              " The top element is " + str(self.peek()))

    def print_all(self):
        while self.top != -1:
            print(self.pop())

    def remove_adjacent(self, input_str):
        print("\nThe input string is:", input_str)
        result = ""
        for character in input_str:
            if self.length() > 0 and self.peek() == character:
                self.pop()
            else:
                self.push(character)
        s_temp = Stack()
        while self.length() > 0:
            element = self.pop()
            s_temp.push(element)
        while s_temp.length() > 0:
            result += s_temp.pop()
        print("The string after removing adjacent duplicates is:", result)
        return result

    def bracket_check(self, input_str):
        print("\nThe input string is:", input_str)
        pairs = {')': '(', '}': '{', ']': '['}
        for character in input_str:
            # Push into stack if character is an opening bracket
            if character in pairs.values():
                self.push(character)
            # If character is a closing bracket, check match
            elif character in pairs:
                if self.length() == 0 or self.peek() != pairs[character]:
                    return False
                self.pop()
        # Return True if stack is empty, else False
        return self.length() == 0


class CircularQueue:
    def __init__(self):
        self.data = [None] * 5
        self.head = 0
        self.tail = 0
        self.max_size = 5

    def enqueue(self, newData):
        if self.length() == self.max_size:
            raise OverflowError("Cannot insert into a full circular queue.")
        print("Enqueue the data " + str(newData))
        ind_tail = self.tail % self.max_size
        self.data[ind_tail] = newData
        self.tail += 1
        print("Now the new tail is " + str(self.tail) +
              " The index used for the tail is " + str(ind_tail))

    def dequeue(self):
        if self.length() == 0:
            raise IndexError("Cannot delete from an empty circular queue.")
        ind_head = self.head % self.max_size
        removed = self.data[ind_head]
        self.head += 1
        print("Dequeue the data " + str(removed))
        print("Now the new head is " + str(self.head) +
              " The index used for the head is " + str(ind_head))
        return removed

    def peek(self):
        if self.length() == 0:
            raise IndexError("Can't peek from an empty queue")
        print("Peek the head")
        ind_head = self.head % self.max_size
        return self.data[ind_head]

    def length(self):
        return self.tail - self.head

    def print_message(self):
        print("The circular queue size is " + str(self.length()) +
              " The first element is " + str(self.peek()) +
              " The head ind is now " + str(self.head) +
              " The tail ind is now " + str(self.tail))

    def print_all(self):
        while self.length() > 0:
            print(self.dequeue())


def run_1():
    q = Queue()
    for j in range(10, 20):
        q.enqueue(50 - j)
    q.print_message()
    for i in range(10, 16):
        q.dequeue()
    q.print_message()
    q.print_all()


def run_2():
    s = Stack()
    for i in range(1, 9):
        s.push(i)
    s.print_message()
    for i in range(1, 5):
        s.pop()
    s.print_message()
    s.print_all()


def run_3():
    q2 = Queue()
    for i in range(0, 5):
        q2.enqueue(i)
    q2.reverse()


def run_4():
    cq = CircularQueue()
    for k in range(-5, 5):  # smaller range to avoid overflow
        cq.enqueue(k)
    cq.print_message()
    for i in range(3):
        cq.dequeue()
    cq.print_message()
    cq.print_all()


def run_5():
    s2 = Stack()
    s2.remove_adjacent("dsallasg")
    s2.remove_adjacent("abccbadd")


def run_6():
    s3 = Stack()
    print("(abc) is valid?", s3.bracket_check("(abc)"))
    s4 = Stack()
    print("d[sa]l(g) is valid?", s4.bracket_check("d[sa]l(g)"))
    s5 = Stack()
    print("[a{b]c} is valid?", s5.bracket_check("[a{b]c}"))


# Test example
#run_1()

# Test example
#run_2()

# Test example
#run_3()

# Test example
#run_4()

# Test example
#run_5()

# Test example
run_6()