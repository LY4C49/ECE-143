def get_trapped_water(seq: list) -> int:
    """_summary_

    Args:
        seq (list): _description_

    Returns:
        int: _description_
    """

    assert isinstance(seq, list)
    for s in seq:
        assert isinstance(s, int) and s >= 0

    stack = []
    stack.append(0)
    ans = 0
    for i in range(1, len(seq)):
        if seq[i] < seq[stack[-1]]:
            stack.append(i)

        elif seq[i] == seq[stack[-1]]:
            stack.pop(-1)
            stack.append(i)

        else:
            while(stack != [] and seq[i] > seq[stack[-1]]):
                mid = stack.pop(-1)
                if stack != []:
                    h = min(seq[stack[-1]], seq[i])-seq[mid]
                    w = i-stack[-1]-1
                    ans += (h*w)
            stack.append(i)

    return ans


if __name__ == "__main__":
    l = [3, 0, 1, 3, 0, 5]
    print(get_trapped_water(l))
