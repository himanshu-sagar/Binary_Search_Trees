# BinarySearchTrees
## Installation

```bash
pip install BinarySearchTrees
```

## It is a module for Binary Search Tree Data Structures. It contains Methods to create,insert,delete,search,traverse and for many other useful Binary search Tree operations.


```python
class Node:
    def __init__(self, data=None):
        self.left = None
        self.right = None
        self.data = data
```


## Methods
=======================================
1. CreateRoot()

	By Default Creates a Root Node With data=None</br>
	Argument: data for Root Node -- Any value Can be passed,which will be assigned to root Node.</br>
	Returns    : Address of Root Node of BST
  
2. GetLeftChild(Argument)

	Argument: Node of object type</br>
	Returns    : Address of left child of the Node
  
3. GetRightChild(Argument)

	Argument: Node of object type</br>
	Returns    : Address of Right child of the Node
  
4. GetRootValue(Argument)

	Argument: Node of object type</br>
	Returns : Data of the Node passed
  
5. Insert(Argument1,Argument2,Argument3)

	Argument1: Root Node</br>
	Argument2: Data to be Inserted --Can be : homogeneous list, int, float or string</br>
	Argument3: only in case of inserting dictionaries-- To insert dictionary values pass: 'values'</br>
                                                   -- To insert dictionary keys pass: 'keys'</br>
                                                   
	Returns  : Nothing
  
6. Inorder(Argument)

	Argument: Root Node of BST which needs to be traversed</br>
	Returns : List of elements after inorder traversal

7. Preorder(Argument)

	Argument: Root Node of BST which needs to be traversed</br>
	Returns : List of elements after preorder traversal
	
8. Postorder(Argument)

	Argument: Root Node of BST which needs to be traversed</br>
	Returns : List of elements after postorder traversal
	
9. LevelOrder(Argument)

	Argument: Root Node of BST which needs to be traversed</br>
	Returns : List of elements after levelorder traversal

10. Width(Argument)

	Argument: Root Node of BST</br>
	Returns : Maximum width (int) of the a BST tree

11. Height(Argument)

	Argument: Root Node of BST</br>
	Returns : Maximum height (int) of the a BST tree

12. Size(Argument)

	Argument: Root Node of BST</br>
	Returns : Maximum width (int) of the a BST tree

13. MaxOfBST(Argument)

	Argument: Root Node of BST</br>
	Returns : Maximum element present in a BST
	
14. MinOfBST(Argument)

	Argument: Root Node of BST</br>
	Returns : Maximum element present in a BST
	
15. Find(Argument1,Argument2)

	Argument1: Root Node of BST</br>
	Argument2: Element to be searched</br>
	Return : If Found:</br>
			returns Address of Node which contains that element</br>
		 else:</br>
			returns -1</br>
						
16. isEmpty()

	Argument: Root Node of BST</br>
	Returns : If Empty:</br>
			returns True</br>
		else:</br>
			returns False</br>
	
17. InorderPredecessor()

	Argument: Any Node of BST</br>
	Returns : Address of its inorder predecessor
	
18. InorderSuccessor()

	Argument: Any Node of BST</br>
	Returns : Address of its inorder successor
	
19. Delete()

	Argument1: Any key element of BST to be deleted</br>
	Returns : Address of root after deleting the specified node

### License
[MIT](https://choosealicense.com/licenses/mit/)
