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


def validate_brackets(string):
    '''
    This function takes a string and return a boolean value
    that representing whether or not the brackets in the 
    string are balanced

    '''
    
    stack = Stack()

    opening_brackets = ['(', '[', '{']
    closing_brackets = [')', ']', '}']
    bracket_pairs = {'(': ')', '[': ']', '{': '}'}

    for char in string:
        if char in opening_brackets:
            stack.push(char)
        elif char in closing_brackets:
            if stack.is_empty():
                return False
            top = stack.pop()
            if bracket_pairs[top] != char:
                return False

    return stack.is_empty()


    





            






