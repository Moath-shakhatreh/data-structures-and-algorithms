# merge sort
```
Merge Sort is a divide-and-conquer algorithm that recursively divides the input array into two halves, sorts them separately, and then merges the sorted halves to obtain the final sorted array.
```

## Pseudocode
```
ALGORITHM Mergesort(arr)
    DECLARE n <-- arr.length

    if n > 1
      DECLARE mid <-- n/2
      DECLARE left <-- arr[0...mid]
      DECLARE right <-- arr[mid...n]
      // sort the left side
      Mergesort(left)
      // sort the right side
      Mergesort(right)
      // merge the sorted left and right sides together
      Merge(left, right, arr)

ALGORITHM Merge(left, right, arr)
    DECLARE i <-- 0
    DECLARE j <-- 0
    DECLARE k <-- 0

    while i < left.length && j < right.length
        if left[i] <= right[j]
            arr[k] <-- left[i]
            i <-- i + 1
        else
            arr[k] <-- right[j]
            j <-- j + 1

        k <-- k + 1

    if i = left.length
       set remaining entries in arr to remaining values in right
    else
       set remaining entries in arr to remaining values in left
```

## Trace
Sample array [8,4,23,42,16,15]

### Step 1: Initial array [8, 4, 23, 42, 16, 15]
 ```

The length of the array is n = 6 > 1, so the sorting process begins..
```
![Alt text](<Untitled (34).jpg>)

### Step 2: Splitting the array
```
The array is split into two halves:
Left half: [8, 4, 23]
Right half: [42, 16, 15]
```
![Alt text](<Untitled (35).jpg>)
### Step 3: Sorting the left half
```
The left half [8, 4, 23] is recursively sorted using the same steps as above.
```

### Step 4: Splitting the left half
```
The left half [8, 4, 23] is split into two halves:
Left half: [8]
Right half: [4, 23]
```
![Alt text](<Untitled (36).jpg>)

### Step 5: Sorting the left half of the left half
```
The left half [8] is already sorted (base case).
```
### Step 6: Sorting the right half of the left half
```
The right half [4, 23] is recursively sorted using the same steps as above.
```
### Step 7: Splitting the right half of the left half
```
The right half [4, 23] is split into two halves:
Left half: [4]
Right half: [23]
```
![Alt text](<Untitled (37).jpg>)

### Step 8: Sorting the left half of the right half of the left half
```
The left half [4] is already sorted (base case).
```
### Step 9: Sorting the right half of the right half of the left half
```
The right half [23] is already sorted (base case).
```
### Step 10: Merging the left half of the left half and the right half of the left half
```
The merge operation combines the sorted left half [4] and the sorted right half [23] into [4, 23]. and [4,23] with [8]
it become [4,8,23]
```
![Alt text](<Untitled (38).jpg>)
### Step 11: Sorting the right half
```
The right half [42, 16, 15] is recursively sorted using the same steps as above.
```
### Step 12: Splitting the right half
```
The right half [42, 16, 15] is split into two halves:
Left half: [42]
Right half: [16, 15]
```
![Alt text](<Untitled (39).jpg>)

### Step 13: Sorting the left half of the right half
```
The left half [42] is already sorted (base case).
```
### Step 14: Sorting the right half of the right half
```
The right half [16, 15] is recursively sorted using the same steps as above.
```
### Step 15: Splitting the right half of the right half
```
The right half [16, 15] is split into two halves:
Left half: [16]
Right half: [15]
```
![Alt text](<Untitled (40).jpg>)
### Step 16: Sorting the left half of the right half of the right half
```
The left half [16] is already sorted (base case).
```
### Step 17: Sorting the right half of the right half of the right half
```
The right half [15] is already sorted (base case).
```
### Step 18: Merging the left half of the right half and the right half of the right half
```
The merge operation combines the sorted left half [16] and the sorted right half [15] into [15, 16]. and [15,16] with [42]
it became [15,16,42]
```
![Alt text](<Untitled (41).jpg>)
### Step 20: Merging the sorted left half and the sorted right half
```
The merge operation combines the sorted left half [4, 8, 23] and the sorted right half [15,16,42] 
```
### Step 21: Final sorted array
```
The array is sorted into [4, 8, 15, 16, 23, 42].
```
![Alt text](<Untitled (42).jpg>)