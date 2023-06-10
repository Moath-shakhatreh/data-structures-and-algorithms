class Node :
    def __init__(self,value=None,next=None):
        self.value = value
        self.next = next

class Stack:
    def __init__(self,top=None):
        self.top = top

        

    def push(self,value):
        '''
        This method adds a new node with that value 
        to the top of the stack with an O(1) Time performance.
 
        '''
        node = Node(value)

        if self.top == None :
            self.top = node
        else:
            node.next = self.top
            self.top = node



    def pop(self):
        '''
        This method returns the value from node from
        the top of the stack and Removes the node from the
        top of the stack

        '''
        if self.top is None:
            raise IndexError("The stack is empty!!")
        else:
            temp= self.top
            self.top = temp.next
            temp.next = None
            return temp.value


    def peek(self):
        '''
        Returns Value of the node located at the top of the stack

        '''
        if self.top == None:
            raise IndexError("The stack is empty!!")
        else:
            return self.top.value
        

    def is_empty(self):
        '''
        this method return Boolean indicating whether or not the stack is empty.
        
        '''
        if self.top == None:
            return True
        else:
            return False

    def __str__(self):
        current=self.top
        string=""
        while current:
            string+=f"{current.value}"
            string+=" -> "
            current=current.next
        return string+"None"    
    

    

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


if __name__ ==  "__main__":
    # node_1 = Node('ahmad')
    stack_01= Stack()
    stack_01.pop()
    # print(stack_01)
    # stack_01.peek()
    # stack_01.push(2)
    # print(stack_01.is_empty())
    # print(stack_01.peek())

    # q=Queue()
    # print(q.is_empty())
    # print(q.dequeue())
    # q.enqueue("hi")
    # print(q.peek())
    # q.enqueue("welcome")
    # q.enqueue("bye")
    # q.dequeue()
    # print(q)
    # print(q.front.value)
    # print(q.back.value)
    # print("deleted element is ",q.dequeue())#deleted node value
    # print(q)