import Lab3

print("Test_Lab3")


def test_bubble_sort_ascending():
    result = []
    input_arr = [64, 34, 25, 12, 22, 11, 90]
    test_arr = [11, 12, 22, 25, 34, 64, 90]

    result = Lab3.bubble_sort(input_arr, Lab3.SORT_ASCENDING)

    assert (result == test_arr)

def test_bubble_sort_descending():
    result = []
    input_arr = [64, 34, 25, 12, 22, 11, 90]
    test_arr = [90, 64, 34, 25, 22, 12, 11]

    result = Lab3.bubble_sort(input_arr, Lab3.SORT_DESCENDING)

    assert (result == test_arr)

def test_bubble_sort_invalid():
    exResult = 0
    input_arr = []

    result = Lab3.bubble_sort(input_arr, 3)

    assert (result == exResult)

def test_bubble_sort_not_integers():

    exResult = 2
    input_arr = [1,3,"a",2,4,5,6]

    result = Lab3.bubble_sort(input_arr, 0)

    assert (exResult == result)

def test_more_equal():

    exResult = 1
    input_arr = [90, 64, 34, 25, 22, 12, 11, 11, 33, 33]

    result = Lab3.bubble_sort(input_arr,0)

    assert (exResult==result)
