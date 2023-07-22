# Challenge Title
Hash Table Implementation

## Approach & Efficiency
The time complexity of most of the methods in the HashTable class is close to O(1) on average, assuming there are no significant collisions. but, in the worst case scenario, where there are many collisions, the time complexity can become O(n), where n is the number of elements in the hash table.

The space complexity of the HashTable class is generally O(n), where n is the number of elements in the hash table, considering the space required to store the key-value pairs and the list of keys. The __hash method has a space complexity of O(1), as it only uses a constant amount of memory to compute the hash code

## Solution
[Solution](./hash__tables.py)