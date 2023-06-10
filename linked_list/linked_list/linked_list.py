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


    def zip_lists(self,list_1 ,list_2 ):
        '''
        This function Zip the two linked lists together into one so 
        that the nodes alternate between the two lists and return 
        a reference to the the zipped list.
        '''
        if list_1.head == None:
            return list_2
        if list_2.head == None:
            return list_1
        
        current_1 = list_1.head
        current_2 = list_2.head
        while current_1 != None and current_2 != None:
            next1 = current_1.next
            next2 = current_2.next
            current_1.next = current_2
            current_2.next = next1 or next2
            current_1 = next1
            current_2 = next2

        return list_1
        
         
        
        
        
        # current_1 = list_1.head
        # current_2 = list_2.head
        # zipped_list = LinkedList()
        # current = zipped_list.head
        # current = current_1
        # return zipped_list
        # current = current_1
        # return zipped_list
        
        # if current_1 is None and current_2 is None:
        #     return 
        # elif current_1 is None:
        #     current = current_2
        #     current_2 = current_2.next
        # elif current_2 is None :
        #     current = current_1
        #     current_1 = current_1.next
        # return zipped_list

        # while True:
            
        #     if current_1 is None and current_2 is None:
        #      return zipped_list
        #     elif current_2 is None :
        #      current = current_1.next
        #      current_1 = current_1.next
        #      current = current.next
        #     elif current_1 is None:
        #      current = current_2
        #      current_2 = current_2.next
        #      current = current.next
        #     return zipped_list
           
           
           

    

             
           


if __name__ == '__main__':
   
    N_1_c = Node(33)
    N_1_b = Node(22,N_1_c)
    N_1_a = Node(11,N_1_b)
    lis_1 = LinkedList(N_1_a)

    N_2_c = Node(66)
    N_2_b = Node(55,N_2_c)
    N_2_a = Node(44,N_2_b)
    lis_2 = LinkedList(N_2_a)

    print(lis_1.to_string())
    print(lis_2.to_string())
    print(LinkedList().zip_lists(lis_1,lis_2).to_string())

    # print(l.to_string())
    
    # moath = Node('moath')
    # print(moath.value)
    # # ahamd = Node('ahmad',moath)
    # # lH = LinkedList()
    # lH = LinkedList(moath)
    # # lH.insert('same')
    # print(lH.include('vvv'))
    # lH.append('yaman')
    # lH.append('feras')
    # lH.insert_before('yaman','yazeed')
    # lH.insert_after('yazeed','samah')
    # print(lH.to_string())
    # print(lH.head.value)
    # print(lH.kth_from_end(4))
    # print(lH.linkedlist_middle())
    
    
    
    
    

    