# insert sort
insertion sort algorithm consists of two main parts: the Insert function, which inserts a value into the sorted portion of the array, and the InsertionSort function, which sorts the entire array using the Insert function.

## Pseudocode
```
Insert(int[] sorted, int value)
  initialize i to 0
  WHILE value > sorted[i]
    set i to i + 1
  WHILE i < sorted.length
    set temp to sorted[i]
    set sorted[i] to value
    set value to temp
    set i to i + 1
  append value to sorted

InsertionSort(int[] input)
  LET sorted = New Empty Array
  sorted[0] = input[0]
  FOR i from 1 up to input.length
    Insert(sorted, input[i])
  return sorted
```

## Trace
Sample array [8,4,23,42,16,15]


### step_1 :
```
Create an empty array to hold the sorted elements.

Sorted Array: []
```
### Step 2: Insert the first element
```
Since the sorted array is empty, we directly insert the first element of the input array.

Input Array: [8, 4, 23, 42, 16, 15]
Sorted Array: [8]
```
### Step 3: Insert the remaining elements
```
Starting from index 1, iterate through the input array and call the Insert function to insert each element into the sorted array.
``` 
### let's explain how insert function work :
```
The Insert function takes two parameters: sorted, which represents a sorted array, and value, which is the element to be inserted into the sorted array. Here's how the function works:

Initialize i to 0: This variable i is used to iterate through the sorted array.

While value > sorted[i]: This loop continues as long as the value is greater than the current element at index i in the sorted array. It is used to find the correct position to insert the value in the sorted array.

Set i to i + 1: Once the correct position is found, this step increments i to move to the next element in the sorted array.

While i < sorted.length: This loop iterates from the current position of i to the end of the sorted array.


Set temp to sorted[i]: This temporary variable temp is used to store the current element at index i in the sorted array.


Set sorted[i] to value: The current element at index i is replaced with the value that needs to be inserted.


Set value to temp: The value that was initially at index i is assigned to value so that it can be moved to the next position in the sorted array.


Set i to i + 1: i is incremented to move to the next position in the sorted array.


Append value to sorted: Once the correct position is found, and the necessary elements are shifted, the value is appended to the sorted array.
```
now let's continue

```
Insert 4 into the sorted array:
Input Array: [8, 4, 23, 42, 16, 15]
Sorted Array: [4, 8]

Insert 23 into the sorted array:
Input Array: [8, 4, 23, 42, 16, 15]
Sorted Array: [4, 8, 23]

Insert 42 into the sorted array:
Input Array: [8, 4, 23, 42, 16, 15]
Sorted Array: [4, 8, 23, 42]

Insert 16 into the sorted array:
Input Array: [8, 4, 23, 42, 16, 15]
Sorted Array: [4, 8, 16, 23, 42]

Insert 15 into the sorted array:
Input Array: [8, 4, 23, 42, 16, 15]
Sorted Array: [4, 8, 15, 16, 23, 42]

Step 4: Return the sorted array
The sorting process is complete. The sorted array now contains the elements in ascending order.

Final Sorted Array: [4, 8, 15, 16, 23, 42]
```

## Effeciency

Time Complexity:

for the insert function it's O(n), as it may need to shift all the elements to the right in the sorted list.
Therefore, the overall time complexity of the InsertionSort function is O(n^2).

Space Complexity:

The space complexity of the Insert function is O(1) since it only uses a constant amount of additional space for the temp variable.
The space complexity of the InsertionSort function is O(n) since it creates a new sorted list
Therefore, the overall space complexity of the algorithm is O(n).