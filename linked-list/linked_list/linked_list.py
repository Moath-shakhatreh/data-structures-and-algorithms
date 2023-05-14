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


if __name__ == '__main__':
    
    moath = Node('moath')
    ahamd = Node('ahmad',moath)
    lH = LinkedList()
    print(lH.head)
    lH = LinkedList(ahamd)
    lH.insert('same')
    print(lH.include('vvv'))
    print(lH.to_string())
    m = lH.head.next
    print(m.value)
    
    
    
    

    