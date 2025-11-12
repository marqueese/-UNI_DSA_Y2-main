#Implement a Binary Search tree

#Step 1: Define the basic unit of a dynamic data structure, the Node class with its initialiser. A BST (Binary Search Tree) consists of nodes, and each node
#has at least three parts: 
#1. value (stores the key for indexing, where the keys and data are separately stored), 
#2. left (stores the reference to the left child -root of the left subtree), 
#3. right (stores the reference to the right child - root of the right subtree).

class Node:

    def __init__(self, key):
        self.left = None # root to the left 
        self.right = None # root to the right 
        self.value = key # stores the key for indexing  

#Step 2: Define the BST class and its initialiser. Root is the reference to the first node; when it is 'None,' the BST is considered empty

class BST:
    
    def __init__(self):
        self.root = None  # when root = None its empty 

#Step 3: Implement the Insert method (input argument: key). A new Node containing the key value is created and inserted into the BST, ensuring
#compliance with the BST's definition. Here a recursive implementation is given.

    def insert (self, key):
        if self.root is None: # root is empty 
            self.root  = Node(key) # 
        else:
            self._insert(self.root, key)

    def _insert(self, current_node, key):

        if key < current_node.value: # the node value is less than the key eg 10 < 30 
            if current_node.left is None:  # Stopping case - if the subtree is empty, insert a new node to the empty space
                current_node.left = Node(key)
            else:
                self._insert(current_node.left, key) # if the subtree contains anyything insert it to the left subtree
        elif key > current_node.value:# if the key is greater then the current value eg 30 > 20 
            if current_node.right is None:
                current_node.right = Node(key)
            else:
                self._insert(current_node, key)
        else:
            print("Key is already in the BST")

                

#Step 4: Implement the Search method (input argument: key). Traverse the BST following its search rules until a leaf node is reached 
#to locate the target. Here a recursive implementation is given.

    def search(self, key):
        return self._search(self.root, key)

    def _search(self, current_node , key):
        if current_node == None: # node is empty 
            return False
        if key == current_node.value: # if the key / value == currrent node value eg 5 = 5    
            return True
        elif key < current_node.left: #if the key is less than everything return the furthest left node and the key 
            return self._search(current_node.left, key)
        else: #if the key is greater than everything return the furthest right node and the key 
            return self._search(current_node.right, key) 


#Step 5: Implement the Delete method (input argument: key). Traverse the BST following its search rules until a leaf node is reached to locate the target and
#delete the target. There are three cases for deletion - when the node to delete has no child/subtree, one child/subtree, or two children/subtrees. Here a
#recursive implementation is given.

    def delete(self, key):
        return self._delete(self.root, key)

    def _delete(self, current_node, key):
        if current_node is None: # current node is false
            return current_node

        if key < current_node: # if the value is smaller than the left hand node delete left
            current_node.left = self._delete(current_node.left, key)
        elif key > current_node: # # if the value is greater than the right hand node delete right
            current_node.right = self._delete(current_node.right, key)
        else: #node with only one child or no child
            if current_node.left is None:
                temp = current_node.right
                current_node = None 
                return temp
            elif current_node.right is None:
                temp = current_node.left
                current_node = None 
                return temp
                # Node with two children: Get the inorder successor(smallest/leftmost node in the right subtree) to replace the value of thedeleted node
                temp = self._min_value_node(current_node.right)
                # Copy the inorder successor's content to this node
                current_node.value = temp.value
                # Delete the inorder successor
                current_node.right = self._delete(current_node.right, temp.value)
            return current_node

    def _min_value_node(self, node):
        # Locate the smallest/leftmost node in the right subtree
        current = node
        while current.left is not None:
            current = current.left
        return current


#Step 6: Implement the Traverse method to output all data items (here keys are printed for simplicity) in the BST. There are two types of traversals:
#breadth-first traversal and depth-first traversal, which includes preOrder,inOrder, and postOrder traversal

    def preorder(self):
        self._preorder(self.root)
        print()

    def _preorder(self, current_node):
        if current_node is not None:
            print(current_node.value, end='')
            self._preorder(current_node.left)
            self._preorder(current_node.right)

#Step 1: Consider implementing the traversal methods iteratively, which will
#keep track of the nodes using a stack. For the preOrder traversal (VLR), after
#visiting a node's value, we push its right and then its left child onto the stack. Given the nature of a stack - FILO, the left child will be the first to be popped.

    def preorder_iter(self):
        if not self.root:  #if the root is empty return nothing
            return []
        stack, output = [self.root], [] # initialist 2 arrays 
        while stack: # run whilst theres items in the stack 
            node = stack.pop() # pop the node and save it to a new variable 
            if node:
                output.append(node.value)
            if node.right:
                stack.append(node.right)
            if node.left:
                stack.append(node.left)
        print(output)

    
    def inorder(self, key):
        return self._inorder(self.root)
        print()

    def _inorder(self, current_node):
        if current_node is not None: #current node is not empty
            self._inorder(current_node.left)
            print(current_node.value, end='')
            self._inorder(current_node.right)
            
#Step 2: For the inOrder traversal (LVR), we keep pushing the left child nodes
#onto the stack. When a node has no left child (or its left child is already visited),
#its value will be visited and its right child will be pushed onto the stack.


        
    def postorder(self):
        self._postorder(self.root)
        print() # for new line
    
    def _postorder(self, current_node):
        if current_node is not None:
            self._postorder(current_node.left)
            self._postorder(current_node.right)
            print(current_node.value, end='')

    def bft(self):
        result = [] #initialise array 
        queue = [self.root] # innitialise the queue 
        while queue: #while there are items in the queue run 
            current_node = queue.pop(0) # recieve the current node and delete it at the same time
            if current_node:
                result.append(current_node.value)
                queue.append(current_node.left)
                queue.append(current_node.right)
        print(result)


def main():
    bst = BST()
    bst.insert(50)
    bst.insert(30)
    bst.insert(20)
    bst.insert(40)
    bst.insert(70)
    bst.insert(60)
    bst.insert(80)
    print("Inorder traversal:")
    bst.inorder()
    print("Preorder traversal:")
    bst.preorder()
    print("Postorder traversal:")
    bst.postorder()
    print("Breadth-first traversal:")
    bst.bft()
    print("Is 40 in the tree?", bst.search(40))
    print("Is 100 in the tree?", bst.search(100))
    print("Deleting 20")
    bst.delete(20)
    print("Inorder traversal after deleting 20:")
    bst.inorder()

main()