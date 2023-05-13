class Node():
    def __init__(self,value,next=None) :
        self.value = value
        self.next = next

class LinkedList():
    def __init__(self,head = None) :
        self.head = head

    def insert(self,value):
        new_node = Node(value)
        new_node.next = self.head
        self.head = new_node

    def include(self,value):
        current = self.head
        while current :
            if current.value == value:
             return True
            else :
             current = current.next
        return False

    def to_string(self):
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
    
    
    
    

    