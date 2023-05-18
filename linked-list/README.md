# Singly Linked Lists
Creating singly linked list with properites and methods to insert nodes to the list , showing all list nodes and finding the kth node from the tail in the linked list.

## Whiteboard Process
>Normal insert
![insertWhiteboard](./insert.jpg)
>Adding
![adding](./adding.jpg)
>Insert_befor
![insert_before](./insert_before.jpg)
>Insert_after
![insert_after](./insert_after.jpg)
>kth_from_end
![kth_from_end](./kth_.jpg)
## Approach & Efficiency

BigO:
```
### Normal insert:

time: O(1)
space: O(1)

### adding ,insert_befor and insert_after

time: O(n) where n the iteration number until we find the specific value
space: O(1)

### kth_from_end:

time: O(n) where n the number of iteration depend on k
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

def kth_from_end(self,k):
        '''
        function that take argument: a number, k,
        as a parameter and Return the node’s value 
        that is k places from the tail of the linked list.
        '''

        length = 0
        current = self.head
        while current:
            length += 1
            current = current.next
        
        if k >= length :
           return "Out of range"
        
        if k < 0 :
           return "Please inter a positive index"
        
        round = length - k -1
        current = self.head

        while round != 0 :
           current = current.next
           round-=1
        return current.value
    

           
    def linkedlist_middle (self):       # Stretch Goal
        '''
        function that return the value of
        the node in the middle of the linked
        list
        '''
        length = 0
        current = self.head
        while current:
            length += 1
            current = current.next
        length = length//2

        current = self.head
        while length != 0 :
           current = current.next
           length -=1
        return current.value
```

