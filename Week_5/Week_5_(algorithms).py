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
    def inorder_iter(self):
        stack, output = [], []
        current = self.root
        while current or stack:
            while current:
                stack.append(current)
                current = current.left
            current = stack.pop()
            output.append(current.value)
            current = current.right
        print(output)

        
    def postorder(self):
        self._postorder(self.root)
        print() # for new line
    
    def _postorder(self, current_node):
        if current_node is not None:
            self._postorder(current_node.left)
            self._postorder(current_node.right)
            print(current_node.value, end='')

#Step 3: For the postOrder traversal (LRV), we use two stacks. The first stack is used to traverse all the nodes and sort their sequence before pushing them
#onto the second stack. Once all the nodes have been visited and the first stack is empty, we visit and output the values of the nodes from the second stack,
#following FILO."

    def postorder_iter(self):
        if not self.root:
            return []
        stack1, stack2 = [self.root], []
        while stack1:
            node = stack1.pop()
            stack2.append(node)
            if node.left:
                stack1.append(node.left)
            if node.right:
                stack1.append(node.right)
        output = []
        while stack2:
            node = stack2.pop()
            output.append(node.value)
        print(output)

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


#3. Design an algorithm to traverse the BST and count the total number of nodes.

    def count_nodes(self):
        return self._count_nodes(self.root)
    
    def _count_nodes(self, current_node):
        if current_node is None:
            return 0
        return 1 + self._count_nodes(current_node.left) + self._count_nodes(current_node.right)

#4. Create an algorithm to count leaf nodes (nodes with no children) in the BST.

    def count_leaf_nodes(self):
        return self._count_leaf_nodes(self.root)
    
    def _count_leaf_nodes(self, current_node):
        if current_node is None:
            return 0
        if current_node.left is None and current_node.right is None:
            return 1
        return self._count_leaf_nodes(current_node.left) + self._count_leaf_nodes(current_node.right)
    
#5. Design an algorithm to determine if two BSTs are identical, meaning they have the same structure and identical values at corresponding nodes.

    def are_identical(self, other_tree):
        return self._are_identical(self.root, other_tree.root)

    def _are_identical(self, node_a, node_b):
    # Both nodes are None, so the trees under these nodes are identical.
        if node_a is None and node_b is None:
            return True
        # One node is None, the other is not, trees are not identical.
        if node_a is None or node_b is None:
            return False
        # Both nodes exist but have different values, trees are not identical.
        if node_a.value != node_b.value:
            return False
        # Recursively compare left and right subtrees. 
        return (self._are_identical(node_a.left, node_b.left) and self._are_identical(node_a.right, node_b.right))
    
#6. (Advanced) Design an algorithm to minimise the height of a BST (creating a balanced BST with the same nodes).

#tep1: To minimise the height of a BST is similar to creating a balanced BST. First we traverse the tree to collect all the nodes in sorted order (inOrder traversal)
    def inorder_traversal(self, node, nodes):
        if node is not None:
            self.inorder_traversal(node.left, nodes)
            nodes.append(node.value)
            self.inorder_traversal(node.right, nodes)   

#Step2: Using the sorted nodes, we build a balanced BST by recursively finding the middle element and making it the root, which applies the same for the left
#and right sublists to create left and right subtrees. 
    def sorted_list_to_bst(self, nodes):
        if not nodes:
            return None
        mid = len(nodes) // 2
        root = Node(nodes[mid])
        root.left = self.sorted_list_to_bst(nodes[:mid])
        root.right = self.sorted_list_to_bst(nodes[mid+1:])
        return root
    
#Step3: Merge the two methods to create the final method. 
    def balance_bst(self):
        nodes = []
        self.inorder_traversal(self.root, nodes)
        self.root = self.sorted_list_to_bst(nodes)

#Step4: Test the method with some testing cases, where the function to output the height should be first defined and used. 
    def height(self):
        return self._height(self.root)
    
    def _height(self, root):
        if root is None:
            return 0
        return max(self._height(root.left), self._height(root.right)) + 1