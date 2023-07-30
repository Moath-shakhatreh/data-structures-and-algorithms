import pytest
from hash__tables import HashTable


def test_hash_method():
  expected = 652
  hash = HashTable()
  actual = hash._HashTable__hash('d')
  assert expected == actual

def test_Retrieving_based_on_a_key_returns_the_value_stored():
  hash = HashTable()
  hash.set('m','k')
  expected = 'k'
  actual = hash.get('m')
  assert actual == expected

def test_Successfully_returns_null_for_a_key_that_does_not_exist():
    hash = HashTable()
    hash.set('m','k')
    actual = hash.get('f')
    expected = None
    assert actual == expected

def test_Successfully_returns_a_list_of_all_unique_keys_that_exist_in_the_hashtable():
    hash = HashTable()
    hash.set('m','k')
    hash.set('n','q')
    actual = hash.keys
    expected = ['m','n']
    assert actual == expected

def test_Successfully_handle_a_collision_within_the_hashtable():   # I made the size equal to 1 to ensure there are a collisions
    hash = HashTable(size=1)
    hash.set('m','q')
    hash.set('d','k')
    g1 = hash.get('m')
    g2 = hash.get('d')
    actual = g1 + g2
    expected = 'qk'
    assert actual == expected

def test_Successfully_retrieve_a_value_from_a_bucket_within_the_hashtable_that_has_a_collision():  # I made the size equal to 1 to ensure there are a collisions
    hash = HashTable(size=1)
    hash.set('m','q')
    hash.set('d','k')
    g1 = hash.get('m')
    g2 = hash.get('d')
    actual = g1 + g2
    expected = 'qk'
    assert actual == expected

def test_hash_range():
    ht = HashTable(size=1000)  # Large size to spread out the keys
    key = "test_key"
    hashed_value = ht._HashTable__hash(key)

    assert hashed_value > 0
    assert hashed_value <  1000
