# Code Challenge: Class 15 + 16 : Binary Tree and BST Implementation

## Whiteboard Process
>Maximum value whiteboard:
![witeboard](./Tree/Untitled%20(23).jpg)

## Approach & Efficiency
```
For maximum_value method:
BigO:
Time --------------->  O(n)
Space --------------> O(n)
where n is the number of element in the tree
```
## Solution
```py
class Tnode:
  def __init__(self,value):
    self.value=value
    self.right= None
    self.left = None
   

class Tree:
  def __init__(self):
    self.root=None

  def breadth_first(self):
    if not self.root:
      return self.root
      
    output = []
    queue = Queue()
    queue.enqueue(self.root)

    while not queue.is_empty():
      
      front = queue.dequeue()
      output.append(front.value)
      
      if front.left :
          queue.enqueue(front.left)
          
      if front.right :
          queue.enqueue(front.right) 
          
        
    return output

  def pre_order(self):
    list_ = []
    def _walk(root):
      #root
      list_.append(root.value)

      #left
      if root.left :
        _walk(root.left)
        
      #right
      if root.right :
        _walk(root.right)

    _walk(self.root)
    return list_

  def in_order(self):
    list_ = []  
    def _walk(root):
      #left
      if root.left :
        _walk(root.left)
        
      #root
      list_.append(root.value)

      #right
      if root.right :
        _walk(root.right)

    _walk(self.root)
    return list_
  

  def post_order(self):
    list_ = []  
    def _walk(root):
      #left
      if root.left :
        _walk(root.left)
        
      #right
      if root.right :
        _walk(root.right)

      #root
      list_.append(root.value)

    _walk(self.root)
    return list_


    def maximum_value(self):
    '''
    Findind the maximum value stored in the tree
    '''
    element = self.pre_order()
    return max(element)

  

class binary_search_tree(Tree):


  def Add(self,value):
    '''
    Adds a new node with that value in the correct location in the binary search tree.
    '''
    
    if self.root == None:
      self.root == Tnode(value) 
      return
    
    current = self.root
    while current : 
      if value < current.value: 
        if current.left == None:
          current.left = Tnode(value)
          return
        else:
          current = current.left
          continue

      if value > current.value :
        if current.right == None:
          current.right = Tnode(value)
          return
        else:
          current = current.right
          continue


  
  def Contains(self,value):
    '''
    Returns boolean indicating whether or not the value is in the tree at least once.
    '''
    current = self.root
    if value == current.value: 
      return True
    
    while current : 
      if value < current.value: 
        if current.left == None:
          return False
        elif value == current.left.value :
          return True
        else:
          current = current.left
          continue

      if value > current.value :
        if current.right == None:
          return False
        elif value == current.right.value:
          return True
        else:
          current = current.right
          continue
    return False
    ```