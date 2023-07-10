def Insert(sorted_list, value):
    i = 0
    while value > sorted_list[i]:
        i = i + 1
    while i < len(sorted_list):
        temp = sorted_list[i]
        sorted_list[i] = value
        value = temp
        i = i + 1
    sorted_list.append(value)

def InsertionSort(input_list):
    sorted_list = [input_list[0]]
    for i in range(1, len(input_list)):
        Insert(sorted_list, input_list[i])
    return sorted_list
