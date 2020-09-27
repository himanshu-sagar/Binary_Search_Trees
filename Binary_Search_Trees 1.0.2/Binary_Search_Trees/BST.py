
from collections import deque
from multipledispatch import dispatch

class Node:
    def __init__(self, data=None):
        self.left = None
        self.right = None
        self.data = data
def CreateBST():
    tree=Node()
    return tree
def GetLeftChild(tree):
    return tree.left

def GetRightChild(tree):
    return tree.right

def GetRootValue(tree):
    return tree.data

@dispatch(object,int)
def Insert(root, data):
    if root.data:
        if data < root.data:
            if root.left is None:
                root.left = Node(data)
            else:
                Insert(root.left,data)
        elif data > root.data:
            if root.right is None:
                root.right = Node(data)
            else:
                Insert(root.right,data)
    else:
        root.data = data

@dispatch(object,float)
def Insert(root, data):
    
    if root.data:
        if data < root.data:
            if root.left is None:
                root.left = Node(data)
            else:
                Insert(root.left,data)
        elif data > root.data:
            if root.right is None:
                root.right = Node(data)
            else:
                Insert(root.right,data)
    else:
        root.data = data

@dispatch(object,str)
def Insert(root, data):

    if root.data:
        if data < root.data:
            if root.left is None:
                root.left = Node(data)
            else:
                Insert(root.left,data)
        elif data > root.data:
            if root.right is None:
                root.right = Node(data)
            else:
                Insert(root.right,data)
    else:
        root.data = data

@dispatch(object,list)
def Insert(root,bst_elements):
    n=len(bst_elements)
    
    for i in range(n):
        Insert(root,bst_elements[i])
@dispatch(object,dict,str)
def Insert(root,bst_elements,flag='values'):
    n=len(bst_elements)
    
    if flag=="values":
        for i in bst_elements.values():
            Insert(root,i)
    elif flag=="keys":
        for i in bst_elements.keys():
            Insert(root,i)


def Preorder(tree):
    q=deque()
    n=0
    preorder_values=[]
    while(tree!=None or n!=0):
        if tree!=None:
            preorder_values.append(tree.data)
            q.append(tree)
            n+=1
            tree=tree.left
        else:
            tree=q.pop()
            n-=1
            tree=tree.right 
    return preorder_values
def Inorder(tree):
    q=deque()
    n=0
    inorder_values=[]
    while(tree!=None or n!=0):
        if tree!=None:
            q.append(tree)
            n+=1
            tree=tree.left
        else:
            
            tree=q.pop()
            n-=1
            inorder_values.append(tree.data)
            tree=tree.right
    return inorder_values
   

def Postorder(root):
    postorder_values=[]
    stack = deque()
    stack.append(root)

    out = deque()
    while stack:
        curr = stack.pop()
        out.append(curr.data)
        if curr.left:
            stack.append(curr.left)

        if curr.right:
            stack.append(curr.right)
    while out:
        a=out.pop()
        postorder_values.append(a)
    return postorder_values


def Levelorder(tree):
    q=deque()
    q.append(tree)
    size=1
    levelorder_values=[]
    while size!=0:
        temp=q.popleft()
        size-=1
        levelorder_values.append(temp.data)
        if temp.left!=None:
            q.append(temp.left)
            size+=1
        if temp.right!=None:
            q.append(temp.right)
            size+=1
    return levelorder_values

def Width(root):
    q=deque()
    q.append(root)
    width=0
    size=1
    while size!=0:
        width=max(size,width)
        for i in range(size):
            temp=q.popleft()
            size-=1
            if temp.left!=None:
                q.append(temp.left)
                size+=1
            if temp.right!=None:
                q.append(temp.right)
                size+=1
    return width

def Height(tree):
    if tree==None:
        return 0
    else:
        return max(Height(tree.left),Height(tree.right))+1

def Size(tree):
    if tree==None:
        return 0
    else:
        return 1+Size(tree.left)+Size(tree.right)

def MaxOfBST(tree):
    def maxbststr(tree):
        if tree==None:
            return str(' '*10000)
        else:
            return max(tree.data,max(maxbststr(tree.left),maxbststr(tree.right)))
    def maxbstnum(tree):
        if tree==None:
            return float('-inf')
        else:
            return max(tree.data,max(maxbstnum(tree.left),maxbstnum(tree.right)))
        
    datatype=type(tree.data)
    if datatype==str:
        t=maxbststr(tree)
    elif datatype==float or datatype==int:
        t=maxbstnum(tree)
    return t

def MinOfBST(tree):
    def minbststr(tree):
        if tree==None:
            return str('}'*10000)
        else:
            return min(tree.data,min(minbststr(tree.left),minbststr(tree.right)))
    def minbstnum(tree):
        if tree==None:
            return float('inf')
        else:
            return min(tree.data,min(minbstnum(tree.left),minbstnum(tree.right)))
        
    datatype=type(tree.data)
    if datatype==str:
        t=minbststr(tree)
    elif datatype==float or datatype==int:
        t=minbstnum(tree)
    return t

def SearchingBST(tree,key):
    while(tree!=None):
        if(key==tree.data):
            return tree
        elif(key<tree.data):
            tree=tree.left
        else:
            tree=tree.right

def Find(tree,key):
    flag=SearchingBST(tree,key)
    if flag==None:
        return -1
    else:
        return flag
    
def isEmpty(tree):
    if tree==None:
        return True
    else:
        return False          

def InorderPredecessor(tree):
    while tree and tree.right:
        tree=tree.right
    return tree

def InorderSuccessor(tree):
    while tree and tree.left:
        tree=tree.left
    return tree

def Delete(tree,key):
    
    if tree==None:
        return None
    if tree.left==None and tree.right==None:
        return None
    if Height(tree)==1:
        return None
    if key<tree.data:
        tree.left=Delete(tree.left,key)
        
    elif key>tree.data:
        tree.right=Delete(tree.right,key)
        
    else:
        if Height(tree.left)>Height(tree.right):
            temp1=InorderPredecessor(tree.left)
            tree.data=temp1.data
            tree.left=Delete(tree.left,temp1.data)
        else:
            temp1=InorderSuccessor(tree.right)
            tree.data=temp1.data
            tree.right=Delete(tree.right,temp1.data)
    return tree
        
