import pytest  
from linked_list.linked_list import LinkedList , Node


def test_empty():
    empty_list = LinkedList()
    actual = empty_list.head
    expected = None
    assert actual == expected

def test_insert():
    listHead = LinkedList()
    listHead.insert('ahmad')
    actual = listHead.head.value
    excepted = 'ahmad'
    assert actual  == excepted

def test_head_properity():
    ahmad = Node('ahmad')
    yaman = Node('yaman',ahmad)
    lH = LinkedList(yaman)
    actual = lH.head.value
    expected = 'yaman'
    assert actual == expected

def test_multiple_insert():
    listHead = LinkedList()
    listHead.insert('same')
    listHead.insert('yaman')
    actual_Head = listHead.head.value
    excepted_Head = 'yaman'
    actual_next_node = listHead.head.next.value
    excepted_next_node = 'same'
    assert actual_Head == excepted_Head
    assert actual_next_node  == excepted_next_node

def test_True_If_find_The_Value():
    ahmad = Node('ahmad')
    yaman = Node('yaman',ahmad)
    lH = LinkedList(yaman) 
    value = lH.include('ahmad')       # I choosed "ahmed" as value to check if it exsist 
    actual = value
    expected = True
    assert actual == expected


def test_False_If_find_The_Value():
    ahmad = Node('ahmad')
    yaman = Node('yaman',ahmad)
    lH = LinkedList(yaman) 
    value = lH.include('fahed')       # I choosed "fahed" as value to check if it exsist 
    actual = value
    expected = False
    assert actual == expected
    
def test_values_colliction_of_the_LinkedTest():
    ahmad = Node('ahmad')
    yaman = Node('yaman',ahmad)
    same = Node('same',yaman)
    lH = LinkedList(same)
    actual = lH.to_string()
    expected = '{same} -> {yaman} -> {ahmad} -> None'
    assert actual == expected

def test_adding_Node_To_The_End_Of_The_List():
    ahmad = Node(1)
    lH = LinkedList(ahmad)
    lH.append(2)                 # adding 2 after 1
    actual = lH.to_string()
    expected = '{1} -> {2} -> None'
    assert actual == expected

def test_adding_Multiple_Nodes_To_The_End_Of_The_List():
    ahmad = Node(1)
    lH = LinkedList(ahmad)
    lH.append(2)                  # adding 2 after 1
    lH.append(3)                  # adding 3 after 2
    actual = lH.to_string()
    expected = '{1} -> {2} -> {3} -> None'
    assert actual == expected

def test_inserting_node_before_node_located_in_the_middle_of_linkedlist():
    ahmad = Node(3)
    yaman = Node(2,ahmad)         
    same = Node(1,yaman)
    lH = LinkedList(same)
    lH.insert_before(2,4)          # insert 4 before the middle of the list
    actual = lH.to_string()
    expected = '{1} -> {4} -> {2} -> {3} -> None'
    assert actual == expected

def test_inserting_node_before_in_the_beginning_of_linkedlist():
    ahmad = Node(1)
    lH = LinkedList(ahmad)          
    lH.insert_before(1,0)           # insert 0 in the begining of the list
    actual = lH.to_string()
    expected = '{0} -> {1} -> None'
    assert actual == expected

def test_insert_node_after_node_in_the_middle_of_the_linkedlist():
    ahmad = Node(3)
    yaman = Node(2,ahmad)
    same = Node(1,yaman)
    lH = LinkedList(same) 
    lH.insert_after(2,4)             # insert 4 after the middle node
    actual = lH.to_string()
    expected = '{1} -> {2} -> {4} -> {3} -> None'
    assert actual == expected


def test_insert_node_after_last_node_in_the_linkedlist():
    ahmad = Node(3)
    yaman = Node(2,ahmad)
    same = Node(1,yaman)
    lH = LinkedList(same)
    lH.insert_after(3,4)             # insert 4 to the end of the list
    actual = lH.to_string()
    expected = '{1} -> {2} -> {3} -> {4} -> None'
    assert actual == expected



    

    

