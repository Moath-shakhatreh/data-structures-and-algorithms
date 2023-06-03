class Queue:
    def __init__(self,front=None,back=None):
        self.front = front # first node in th queue
        self.back=back    # last node in queue    

    def  enqueue_(self,value) :
        '''
        adds a new node with that value to the back of the queue with an O(1) Time performance

        '''
        
        if self.back is None:
            self.back = value
            self.front = value
        else:
            self.back.next= value
            self.back = value 



    def dequeue_(self):
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
            return temp
        

    
    
    def __str__(self):
        current=self.front
        string=""
        while current:
            string+=f"{current.name}"
            string+=" -> "
            current=current.next
        return string+"None"



class Animal:
    def __init__(self,name,species,next=None):
        self.name = name
        self.species = species
        self.next = next



class AnimalShelter:
    def __init__(self):
        self.queue1 = Queue() 
        self.queue2 = Queue()

 
    
    def  enqueue(self,name) :
        '''
        adds a new animal 

        '''
        self.queue1.enqueue_(name)
        



    def dequeue(self,pref):
        '''
        Removes the a cat or a dog

        '''
        if self.queue1.front is None:
            raise IndexError("The queue is empty!!")
        else:
            temp = self.queue1.front
            while temp.species != pref :
                
                self.queue2.enqueue_(self.queue1.dequeue_())
                temp = self.queue1.front
                if temp == None:
                    print(f'no {pref} in the shelter')
                    return

                
            if temp.species == pref:
                self.queue1.front = temp.next
                temp.next = None

            current = self.queue1.front
            while current != None:
                self.queue2.enqueue_(self.queue1.dequeue_())
                current = current.next
                
            # # current = self.queue2.front
            # # while current != None:
            # print('ffff')
            # z = self.queue2.dequeue_()
            # self.queue1.enqueue_(z)
            #     # current = current.next


    
            

    

    
if __name__ ==  "__main__":
    Q_1 = AnimalShelter()
    yona = Animal('yona','cat')
    sam = Animal('sam','dog')
    jane = Animal('jane','cat')
    Q_1.enqueue(yona)
    Q_1.enqueue(sam)
    Q_1.enqueue(jane)
    print(Q_1.queue1)

    Q_1.dequeue('dog')
    print(Q_1.queue2)
    Q_1.dequeue('cat')
    print(Q_1.queue2)

    