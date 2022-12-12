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


# if __name__ == "__main__":
#     x= ['100', '100', '110', '010', '111', '000', '110', '010', '011', '000']
#     print(map_bitstring(x=x))
