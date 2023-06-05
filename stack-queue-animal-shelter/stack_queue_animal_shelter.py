class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class Queue:
    def __init__(self):
        self.front = None
        self.back = None

    def enqueue(self, value):
        new_node = Node(value)

        if self.back is None:
            self.back = new_node
            self.front = new_node
        else:
            self.back.next = new_node
            self.back = new_node

    def dequeue(self):
        if self.front is None:
            raise IndexError("The queue is empty!")
        else:
            temp = self.front
            self.front = temp.next
            temp.next = None
            return temp.value

    def __str__(self):
        current = self.front
        string = ""
        while current:
            string += str(current.value.name) + " -> "
            current = current.next
        return string + "None"


class Animal:
    def __init__(self, name, species):
        self.name = name
        self.species = species


class AnimalShelter:
    
    def __init__(self):
        self.dog_queue = Queue()
        self.cat_queue = Queue()

    def enqueue(self, animal):
        if animal.species == "dog":
            self.dog_queue.enqueue(animal)
        elif animal.species == "cat":
            self.cat_queue.enqueue(animal)

    def dequeue(self, pref):
        if pref == "dog":
            return self.dog_queue.dequeue()
        elif pref == "cat":
            return self.cat_queue.dequeue()
        else:
            return None





if __name__ == '__main__':
    animal_shelter = AnimalShelter()

    dog1 = Animal("Buddy", "dog")
    cat1 = Animal("Whiskers", "cat")
    dog2 = Animal("Max", "dog")

    animal_shelter.enqueue(dog1)
    animal_shelter.enqueue(cat1)
    animal_shelter.enqueue(dog2)

    # print(animal_shelter.dequeue("dog"))  
    # print(animal_shelter.dequeue("cat"))  
    # print(animal_shelter.dequeue("dog"))  
    # print(animal_shelter.dequeue("bird"))  # Output: None
    print(animal_shelter.dog_queue)
    print(animal_shelter.cat_queue)
