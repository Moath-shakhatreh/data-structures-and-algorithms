# Singly Linked Lists
Creating singly linked list with properites and methods to insert nodes to the list and showing all list nodes 

## Whiteboard Process
![insertWhiteboard](./insert.jpg)

## Approach & Efficiency
BigO:

time: O(1)

space: O(1)

## Solution

def insert(self,value):

        new_node = Node(value)

        new_node.next = self.head

        self.head = new_node