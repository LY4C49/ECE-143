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


def map_bitstring(x: list) -> dict:
    """_summary_

    Args:
        x (list): _description_

    Returns:
        dict: _description_
    """
    assert isinstance(x, list)
    result = {}

    for s in x:
        assert isinstance(s, str)
        if s in result:
            continue
        len_s = len(s)
        num_0 = 0
        for bit in s:
            assert (bit == "0" or bit == "1")
            if bit == "0":
                num_0 += 1
        if num_0 > int(len_s/2):
            result[s] = 0
        else:
            result[s] = 1

    return result


def gather_values(x: list) -> dict:
    """_summary_

    Args:
        x (list): _description_

    Returns:
        dict: _description_
    """
    assert isinstance(x, list)
    refer = map_bitstring(x)
    result_map = {}
    for s in x:
        if s not in result_map:
            result_map[s] = [refer[s]]
        else:
            result_map[s].append(refer[s])
    return result_map


def threshold_values(seq, threshold=1):
    """_summary_

    Args:
        seq (_type_): _description_
        threshold (int, optional): _description_. Defaults to 1.
    """
    assert isinstance(seq, list)
    assert isinstance(threshold, int) and threshold >= 0
    gathered = gather_values(seq)
    freq = {}

    for key, value in gathered.items():
        freq[key] = len(value)

    # if there is a tie, smaller key will have higher priority!
    # python sort list from small to big, so use negative value to sort.
    # Bigger positive value will have smaller reversed value
    result_list = sorted(freq.items(), key=lambda t: (-t[1], int(t[0], 2)))

    result = {}
    for i, element in enumerate(result_list):
        if i+1 <= threshold:
            result[element[0]] = 1
        else:
            result[element[0]] = 0

    return result


# if __name__ == '__main__':
#     seq = ['1111', '0110', '1001', '0011', '0111', '0100', '0111', '1100', '0011', '0010', '0010', '1010', '1010', '1100', '0110', '0101', '0110', '1111', '1001', '0110', '0010', '1101', '0101', '0010', '0100', '0010', '0000', '0000', '0011', '0110', '0101', '1010', '1011', '1101', '1100', '0111', '1110', '0100', '0110', '1101', '0001', '1110', '0010', '0001', '1010', '1010', '0011', '1000', '0010', '0000',
#            '1010', '1101', '1111', '1000', '1000', '0010', '1010', '0101', '0101', '1101', '0110', '1001', '1100', '1100', '1000', '1010', '0011', '0101', '0101', '0011', '0001', '1010', '0011', '0011', '1101', '1010', '0101', '0011', '1011', '0101', '0000', '1111', '1001', '0101', '1100', '0011', '1111', '1101', '0001', '1111', '1110', '1111', '0001', '0010', '0110', '0100', '0101', '1100', '1110', '1001']
#     print(threshold_values(seq=seq,threshold=3))
