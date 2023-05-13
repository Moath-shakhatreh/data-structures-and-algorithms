import pytest  
from linked_list.linked_list import LinkedList , Node


def test_empty():
    empty_list = LinkedList()
    actual = empty_list.head
    expected = None
    assert actual == expected

# def test_insert():
#     inserted_element = LinkedList().insert('moath')
#     actual = 