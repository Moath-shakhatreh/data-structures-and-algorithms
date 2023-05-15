# Singly Linked Lists
Creating singly linked list with properites and methods to insert nodes to the list and showing all list nodes 

## Whiteboard Process
>Normal insert
![insertWhiteboard](./insert.jpg)
>Adding
![adding](./adding.jpg)
>Insert_befor
![insert_before](./insert_before.jpg)
>Insert_after
![insert_after](./insert_after.jpg)

## Approach & Efficiency
BigO:

### Normal insert
```
time: O(1)
space: O(1)
```
### adding ,insert_befor and insert_after
```
time: O(n) where n the iteration number until we find the specific value
space: O(1)
```
## Solution
``` python
def insert(self,value):

        new_node = Node(value)

        new_node.next = self.head

        self.head = new_node

def append(self,new_value):
       '''
       adds a new node with the given value to the end of the list
       '''
       
       current = self.head
       while current :
          if current.next == None:
            current.next = Node(new_value)
            return 
             
          current = current.next

def insert_before(self,value,new_value):
        '''
        adds a new node with the given new value immediately before the first node that has the value specified
        '''
        new_node = Node(new_value)
        current = self.head

        # Check if the list is empty
        if self.head is None:
            self.head = new_node
            return

        if current.value == value:
           new_node.next = self.head
           self.head = new_node
           return 

        while current.next:
           if current.next.value == value:
            new_node.next = current.next
            current.next = new_node
            return
           current = current.next
        
def insert_after(self,value,new_value):
       '''
       adds a new node with the given new value immediately 
       after the first node that has the value specified
       '''
       new_node = Node(new_value)
       current = self.head

       if self.head is None:
            self.head = new_node
            return

       while current :
          if current.value == value:
             new_node.next = current.next
             current.next = new_node
             return
          current = current.next
```