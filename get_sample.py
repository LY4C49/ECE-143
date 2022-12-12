import random
def get_sample(nbits=3, prob=None, n=1):
    '''
    docstring!
    '''
    """_summary_

    Args:
        nbits (int, optional): _description_. Defaults to 3.
        prob (dict, optional): _description_. Defaults to None.
        n (int, optional): _description_. Defaults to 1.
    """
    assert isinstance(nbits, int) and nbits >= 1
    assert isinstance(prob, dict)
    assert isinstance(n, int) and nbits >= 1

    elements = []
    probability = []

    for key, value in prob.items():
        assert len(key) == nbits
        assert 0 <= value <= 1
        for bit in key:
            assert (bit == "0" or bit == "1")

        elements.append(key)
        probability.append(value)

    assert sum(probability) == 1
    return random.choices(population=elements, weights=probability, k=n)


# if __name__ == '__main__':
#     p = {'010': 0.125,
#         '001': 0.125,
#         '010': 0.125,
#         '011': 0.125,
#         '100': 0.125,
#         '101': 0.125,
#         '110': 0.125,
#         '111': 0.125}
#     print(get_sample(nbits=3, prob=p, n=2))
