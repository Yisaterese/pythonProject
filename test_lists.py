from lists import list_of_integers,duplicate_list_of_integers,eliminate_duplicates_in_list_of_integers,add_third_elements_in_list

def test_list_of_integers():
    my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
    assert list_of_integers() == my_list

def test_duplicating_list_of_integers():
    my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
    assert duplicate_list_of_integers() == my_list


def test_can_eliminate_duplicate_in_list_of_integers():
    my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
    assert eliminate_duplicates_in_list_of_integers() == my_list


def test_can_add_third_elemenst_in_list():
    assert add_third_elements_in_list([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == 18