import pytest

from hashmap_left_join.hashmap_left_join import left_join
from hash_tables.hash__tables import HashTable





def test_if_one_hash_is_empty():
    hash_1 = HashTable()
    hash_2 = HashTable()
    hash_1.set('diligent','employed')
    hash_1.set('fond','enamored')
    actual = left_join(hash_1,hash_2)
    expected = [['diligent', 'employed', 'NULL'], ['fond', 'enamored', 'NULL']]
    assert actual == expected

def test_if_both_hash_table_are_empty():
    hash_1 = HashTable()
    hash_2 = HashTable()
    actual = left_join(hash_1,hash_2)
    expected = []
    assert actual == expected


def test_3():
    hash_1 = HashTable()
    hash_2 = HashTable()

    hash_1.set('diligent','employed')
    hash_1.set('fond','enamored')
    hash_1.set('guide','usher')
    hash_1.set('outfit','garb')
    hash_1.set('wrath','anger')

    hash_2.set('diligent','idle')
    hash_2.set('fond','averse')
    hash_2.set('guide','follow')
    hash_2.set('flow','jam')
    hash_2.set('wrath','delight')

    actual = left_join(hash_1,hash_2)
    expected = [['diligent', 'employed', 'idle'], ['fond', 'enamored', 'averse'], ['guide', 'usher', 'follow'], ['outfit', 'garb', 'NULL'], ['wrath', 'anger', 'delight']]
    assert actual == expected

    
