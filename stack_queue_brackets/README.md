# Multi-bracket Validation.


## Whiteboard Process
![whiteBorad](./Untitled%20(21).jpg)
## Approach & Efficiency
```
BigO:
Time --------------->  O(n)
Space --------------> O(n)
where n is the number of element in the string
```
## Solution
```py
def validate_brackets(string):
    '''
    This function takes a string and return a boolean value
    that representing whether or not the brackets in the 
    string are balanced

    '''
    
    stack = Stack()

    opening_brackets = ['(', '[', '{']
    closing_brackets = [')', ']', '}']
    bracket_pairs = {'(': ')', '[': ']', '{': '}'}

    for char in string:
        if char in opening_brackets:
            stack.push(char)
        elif char in closing_brackets:
            if stack.is_empty():
                return False
            top = stack.pop()
            if bracket_pairs[top] != char:
                return False

    return stack.is_empty()