import pytest
from hash__tables import HashTable


def test_hash_method():
  expected = 652
  hash = HashTable()
  actual = hash._HashTable__hash('d')
  assert expected == actual