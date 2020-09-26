# BinarySearchTrees
# How to Install
---------------------------------------
pip install BinarySearchTrees

---------------------------------------
It is a module for Binary Search Tree Data Structures. It contains Methods to create,insert,delete,search,traverse and for many other useful Binary search Tree operations.
---------------------------------------


class Node:

    def __init__(self, data=None):
    
        self.left = None
        
        self.right = None
        
        self.data = data



# Methods
=======================================
1. CreateRoot()

	By Default Creates a Root Node With data=None
  
	Argument: data for Root Node -- Any value Can be passed,which will be assigned to root Node.
  
	Returns    : Address of Root Node of BST
  
2. GetLeftChild()

	Argument: Node of object type
  
	Returns    : Address of left child of the Node
  
3. GetRightChild()

	Argument: Node of object type
  
	Returns    : Address of Right child of the Node
  
4. GetRootValue()

	Argument: Node of object type
  
	Returns    : Data of the Node passed
  
5. Insert()

	Argument1: Root Node
  
	Argument2: Data to be Inserted --Can be : homogeneous list, int, float or string
  
	Argument3: only in case of inserting dictionaries-- To insert dictionary values pass: 'values'
                                                   -- To insert dictionary keys pass: 'keys'
                                                   
	Returns    : Root Node of the BST
  
6. Inorder()

7. Preorder()

8. Postorder()

9. LevelOrder()

10. Width()

11. Height()

12. Size()

13. MaxOfBST()

14. MinOfBST()

15. Find()

16. isEmpty()

17. InorderPredecessor()

18. InorderSuccessor()

19. Delete()
