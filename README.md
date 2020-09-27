# Binary_Search_Trees
## Installation

```bash
pip install Binary_Search_Trees
#or
import Binary_Search_Trees.BST as bst
#or
from Binary_Search_Trees.BST import *
```

## It is a module for Binary Search Tree Data Structures. It contains Methods to create,insert,delete,search,traverse and for many other useful Binary search Tree operations.


```python
class Node:
    def __init__(self, data=None):
        self.left = None
        self.right = None
        self.data = data
```

```python
from Binary_Search_Trees import BST as bst
```

## Methods
=======================================
1. CreateBST()

	By Default Creates a Root Node With data=None</br>
	Argument: data for Root Node -- Any value Can be passed,which will be assigned to root Node.</br>
	Returns    : Address of Root Node of BST

```python
root=bst.CreateBST()
```

2. GetLeftChild(Argument)

	Argument: Node of object type</br>
	Returns    : Address of left child of the Node
	
```python
bst.GetLeftChild(root)
```

3. GetRightChild(Argument)

	Argument: Node of object type</br>
	Returns    : Address of Right child of the Node

```python
bst.GetRightChild(root)
```

4. GetRootValue(Argument)

	Argument: Node of object type</br>
	Returns : Data of the Node passed

```python
bst.GetRootValue(root)
```

5. Insert(Argument1,Argument2,Argument3)

	Argument1: Root Node</br>
	Argument2: Data to be Inserted --Can be : homogeneous list, int, float or string</br>
	Argument3: only in case of inserting dictionaries-- To insert dictionary values pass: 'values'</br>
                                                   -- To insert dictionary keys pass: 'keys'</br>
                                                   
	Returns  : Nothing

```python
bst.Insert(root,4)# passing integer
bst.Insert(root,'d') #passing character
bst.Insert(root,57.733) # passing float value
```

```python
bst.Insert(root,[4,1,2,7,5,9])# passing list
```

```python
bst.Insert(root,{1:1,2:4,5:25,3:9},'values')# passing dictionary
bst.Insert(root,{1:1,2:4,5:25,3:9},'keys')
```

6. Inorder(Argument)

	Argument: Root Node of BST which needs to be traversed</br>
	Returns : List of elements after inorder traversal

```python
val=bst.Inorder(root)
print(val)
```

7. Preorder(Argument)

	Argument: Root Node of BST which needs to be traversed</br>
	Returns : List of elements after preorder traversal

```python
val=bst.Preorder(root)
print(val)
```

8. Postorder(Argument)

	Argument: Root Node of BST which needs to be traversed</br>
	Returns : List of elements after postorder traversal

```python
val=bst.Postorder(root)
print(val)
```

9. LevelOrder(Argument)

	Argument: Root Node of BST which needs to be traversed</br>
	Returns : List of elements after levelorder traversal

```python
val=bst.LevelOrder(root)
print(val)
```

10. Width(Argument)

	Argument: Root Node of BST</br>
	Returns : Maximum width (int) of the a BST tree

```python
val=bst.Width(root)
print(val)
```

11. Height(Argument)

	Argument: Root Node of BST</br>
	Returns : Maximum height (int) of the a BST tree

```python
val=bst.Height(root)
print(val)
```

12. Size(Argument)

	Argument: Root Node of BST</br>
	Returns : Maximum width (int) of the a BST tree

```python
val=bst.Size(root)
print(val)
```

13. MaxOfBST(Argument)

	Argument: Root Node of BST</br>
	Returns : Maximum element present in a BST

```python
val=bst.MaxOfBST(root)
print(val)
```

14. MinOfBST(Argument)

	Argument: Root Node of BST</br>
	Returns : Maximum element present in a BST

```python
val=bst.MinOfBST(root)
print(val)
```

15. Find(Argument1,Argument2)

	Argument1: Root Node of BST</br>
	Argument2: Element to be searched</br>
	Return : If Found:</br>
			returns Address of Node which contains that element</br>
		 else:</br>
			returns -1</br>

```python
val=bst.Find(root,4)
print(val)
```

16. isEmpty(Argument)

	Argument: Root Node of BST</br>
	Returns : If Empty:</br>
			returns True</br>
		else:</br>
			returns False</br>

```python
val=bst.isEmpty(root)
print(val)
```

17. InorderPredecessor(Argument)

	Argument: Any Node of BST</br>
	Returns : Address of its inorder predecessor

```python
val=bst.InorderPredecessor(root)
print(val.data)
```

18. InorderSuccessor(Argument)

	Argument: Any Node of BST</br>
	Returns : Address of its inorder successor

```python
val=bst.InorderSuccessor(root)
print(val.data)
```

19. Delete(Argument1,Argument2)

	Argument1: Root Node of BST
	Argument2: Any key element of BST to be deleted</br>
	Returns  : Address of root after deleting the specified node
	
```python
t=bst.Delete(root,4)
```

### License
[MIT](https://choosealicense.com/licenses/mit/)
