from subsetsum import find_sums, SubsetSum

def test_find_sum_1_0():
    S = SubsetSum()
    assert S.find_sum_of_n(10, [5, 5, 5, 5, 5], 1) == None

def test_find_sum_1():
    S = SubsetSum()
    assert S.find_sum_of_n(10, [10], 1) == [[10]]

def test_find_sum_2():
    S = SubsetSum()
    assert S.find_sum_of_n(10, [5, 5, 5, 5, 5], 2) == [[5,5]]

def test_find_sum_3_0():
    S = SubsetSum()
    assert S.find_sum_of_n(10, [2, 8, 2, 5, 5, 5, 5, 5], 3) == None

def test_find_sum_3_1():
    S = SubsetSum()
    assert S.find_sum_of_n(15, [5, 5, 5, 5, 5], 3) == [[5,5,5]]

def test_find_sum_3_2():
    S = SubsetSum()
    assert S.find_sum_of_n(12, [2, 8, 3, 3, 4, 5, 5, 5, 5, 5], 3) == [[2,5,5], [3,4,5]]
