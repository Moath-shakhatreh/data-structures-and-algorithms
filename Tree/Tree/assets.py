class Node :
    def __init__(self,value=None,next=None):
        self.value = value
        self.next = next

     

class Queue:
    def __init__(self,front=None,back=None):
        self.front = front # first node in th queue
        self.back=back    # last node in queue    

    def  enqueue(self,value) :
        '''
        adds a new node with that value to the back of the queue with an O(1) Time performance

        '''
        node = Node(value)
        if self.front is None:
            self.back = node
            self.front = node
        else:
            self.back.next= node
            self.back = node 



    def dequeue(self):
        '''
        Removes the node from the front of the queue and
        Returns the value from node from the front of the queue

        '''
        if self.front is None:
            raise IndexError("The queue is empty!!")
        else:
            temp = self.front
            self.front = temp.next
            temp.next = None
            return temp.value
        

    def peek(self):
        '''
        Returns Value of the node located at front of the queue

        '''
        if self.front == None:
            raise IndexError("The queue is empty!!")
        else:
            return self.front.value
        

    def is_empty(self):
        '''
        this method return Boolean indicating whether or not the queue is empty.
        
        '''
        if self.front == None:
            return True
        else:
            return False
    
    
    def __str__(self):
        current=self.front
        string=""
        while current:
            string+=f"{current.value}"
            string+=" -> "
            current=current.next
        return string+"None"