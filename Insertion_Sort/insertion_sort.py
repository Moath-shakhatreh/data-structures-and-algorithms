def Insert(sorted_list, value):
    i = 0
    while value > sorted_list[i]:
        i = i + 1
        if i == len(sorted_list):  # If we reach the end of the list
            break
    sorted_list.insert(i, value)  # Use insert() instead of assignment

def InsertionSort(input_list):
    if len(input_list) == 0:
        return []  # Return an empty list if input is empty

    sorted_list = [input_list[0]]
    for i in range(1, len(input_list)):
        Insert(sorted_list, input_list[i])
    return sorted_list


if __name__ == '__main__' :
    print(InsertionSort([5,12,7,5,5,7]))
