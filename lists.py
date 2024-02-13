
def list_of_integers():
    list1 = []
    for number in range(1, 16):
        list1.append(number)
    return list1

def duplicate_list_of_integers():
    list1 = []
    list2 = []
    for number in range(1, 16):
        list1.append(number)
        list2.append(number)

    return list2.extend(list1)

def eliminate_duplicates_in_list_of_integers():
    list1 = []
    list2 = []
    for number in range(1, 16):
        list1.append(number)
        list2.append(number)
    list2.extend(list1)

    my_set = set(list2)

    return list(my_set)

def add_third_elements_in_list(my_list):
    sum_of_numbers = 0
    for elements in range(2, len(my_list), 3):
        sum_of_numbers += my_list[elements]

    return sum_of_numbers

def sum_third_elements_in_list(my_list):
    sum_of_numbers = 0
    for elements in range(2, len(my_list), 3):
        sum_of_numbers += my_list[elements]

    return sum_of_numbers
