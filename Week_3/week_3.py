from random import sample
class Recursion:
def __init__(self):
self.data = []
self.max_size = 100
def initialise(self):
self.data = sample(range(1, 3 * self.max_size), self.max_size)
def print_all(self):
print("The size of the random array " + str(len(self.data)))
print("Before sorting, the array is " + str(s