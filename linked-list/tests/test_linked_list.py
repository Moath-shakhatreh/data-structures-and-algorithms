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


