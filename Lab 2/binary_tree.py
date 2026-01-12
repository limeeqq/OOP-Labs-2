class Node:
    def __init__(self, data):
        self.data = data   
        self.left = None    
        self.right = None     

class BinaryTree:
    def __init__(self):
        self.root = None

    def add(self, new_data):

        if self.root is None:
            self.root = Node(new_data)
        else:
            self._add_recursive(self.root, new_data)

    def _add_recursive(self, current_node, new_data):
    

        if new_data < current_node.data:
            if current_node.left is None:
                current_node.left = Node(new_data)
            else:
                self._add_recursive(current_node.left, new_data)
        
        elif new_data > current_node.data:
            if current_node.right is None:
                current_node.right = Node(new_data) 
            else:
                self._add_recursive(current_node.right, new_data)
        else:
        
            pass

    def show_tree(self):
    
        print("\nсписок студентів, результат:")
        self._print_preorder(self.root)

    def _print_preorder(self, node):
        if node is not None:
            print(node.data.get_info()) 
            self._print_preorder(node.left) 
            self._print_preorder(node.right)