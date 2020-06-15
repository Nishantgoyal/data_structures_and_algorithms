from polynomial import Polynomial


def test_convert_arr_into_pol():
    inputs = [
        {"input": [], "output":{}},
        {"input": [2, 3, 4], "output":{2: 2, 1: 3, 0: 4}},
        {"input":  [3, 4, 5, 6], "output":{3: 3, 2: 4, 1: 5, 0: 6}},
        {"input": [1, 2], "output":{1: 1, 0: 2}},
    ]
    pol_class = Polynomial()
    for item in inputs:
        pol = pol_class.convert_arr_into_pol(item["input"])
        assert(item["output"] == pol)


def test_polinomial_multiply():
    inputs = [
        {"inp": ([], []), "out":[]},
        {"inp": ([1], [1]), "out":[1]},
        {"inp": ([2, 1], [1]), "out":[2, 1]},
        {"inp": ([2, 1], [2, 1]), "out":[4, 4, 1]},
        {"inp": ([3, 2, 1], [2, 1]), "out":[6, 7, 4, 1]},
        {"inp": ([3, 2, 5], [5, 1, 2]), "out":[15, 13, 33, 9, 10]},
    ]
    for inp in inputs:
        pol_class = Polynomial(inp["inp"][0], inp["inp"][1])
        pol_result = pol_class.polinomial_multiply()
        assert(inp["out"] == pol_result)
