import pytest 
from stack_and_queue.stack_and_queue import Node, Stack , Queue



# Stack Tests

def test_Can_successfully_push_onto_a_stack():
    sH = Stack()
    sH.push('ahmad')
    actual = sH.top.value
    expected = 'ahmad'
    assert actual == expected
    

def test_Can_successfully_push_multiple_values_onto_a_stack():
    sH = Stack()
    sH.push('ahmad')
    sH.push('yaseen')
    sH.push('same')
    actual = sH.top.value
    expected = 'same'
    assert actual == expected

def test_Can_successfully_pop_off_the_stack():
    sH = Stack()
    sH.push('ahmad')
    sH.pop()
    actual = sH.top
    expected = None
    assert actual == expected

def test_Can_successfully_empty_a_stack_after_multiple_pops():
    sH = Stack()
    sH.push('ahmad')
    sH.push('yaseen')
    sH.pop()
    sH.pop()
    actual = sH.top
    expected = None
    assert actual == expected


def test_Can_successfully_peek_the_next_item_on_the_stack():
    sH = Stack()
    sH.push('ahmad')
    sH.push('yaseen')
    sH.peek()
    actual = sH.peek()
    expected = 'yaseen'
    assert actual == expected


def test_Can_successfully_instantiate_an_empty_stack():
    sH = Stack()
    actual = sH.top
    expected = None
    assert actual == expected


def test_Calling_pop_or_peek_on_empty_stack_raises_exception():
    sH = Stack()
    with pytest.raises(IndexError):
        sH.peek()


# Queue Tests

def test_Can_successfully_enqueue_onto_a_queue():
    q = Queue()
    q. enqueue('ahmad')
    actual = q.back.value
    expected = 'ahmad'
    assert actual == expected
    

def test_Can_successfully_enqueue_multiple_values_onto_a_queue():
    q = Queue()
    q.enqueue('ahmad')
    q.enqueue('yaseen')
    q.enqueue('same')
    actual = q.back.value
    expected = 'same'
    assert actual == expected

def test_Can_successfully_dequeue_off_the_queue_the_expected_value():
    q = Queue()
    q.enqueue('ahmad')
    q.enqueue('yaseen')
    actual = q.dequeue()
    expected = 'ahmad'
    assert actual == expected



def test_Can_successfully_peek_a_queue_seeing_the_expected_value():
    q = Queue()
    q.enqueue('ahmad')
    q.enqueue('yaseen')
    actual = q.peek()
    expected = 'ahmad'
    assert actual == expected
    

def test_Can_successfully_empty_a_queue_after_multiple_dequeues():
    q = Queue()
    q.enqueue('ahmad')
    q.enqueue('yaseen')
    q.dequeue()
    q.dequeue()
    actual = q.front
    expected = None
    assert actual == expected


def test_Can_successfully_instantiate_an_empty_queue():
    q = Queue()
    actual = q.front
    expected = None
    assert actual == expected


def test_Calling_pop_or_peek_on_empty_queue_raises_exception():
    q = Queue()
    with pytest.raises(IndexError):
        q.peek()



  
