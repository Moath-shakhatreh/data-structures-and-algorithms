class Node():
    '''
    This class used to crate nodes with properities of 
    vlaue(Node value) and next(indicates next node object)
    '''
    def __init__(self,value,next=None) :
        self.value = value
        self.next = next

class LinkedList():
    '''
    This class is used to chose the node that will be 
    the head of the linkedList, showing the nodes in 
    list and finally insert a node to the list 
    '''
    def __init__(self,head = None) :
        self.head = head

    def insert(self,value):
        '''
        insert a new node to the linked list
        '''
        new_node = Node(value)
        new_node.next = self.head
        self.head = new_node

    def include(self,value):
        '''
        Check if the input value are exist in the value
        of the nodes that are in the linkedlist(return 
        False if exist and True if not) 
        '''
        current = self.head
        while current :
            if current.value == value:
             return True
            else :
             current = current.next
        return False

    def to_string(self):
        '''
        Showing all linkedlist nodes values i astring
        '''
        a = ''
        current = self.head
        while current:
          b = f'{{{current.value}}} -> '
          a = a + b
          current = current.next
        a = a + 'None'
        return a
    
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

    

             
           


if __name__ == '__main__':
    
    moath = Node('moath')
    # ahamd = Node('ahmad',moath)
    # lH = LinkedList()
    lH = LinkedList(moath)
    # lH.insert('same')
    print(lH.include('vvv'))
    lH.append('yaman')
    lH.append('feras')
    lH.insert_before('yaman','yazeed')
    lH.insert_after('yazeed','samah')
    print(lH.to_string())
    print(lH.head.value)
    
    
    
    
    

    