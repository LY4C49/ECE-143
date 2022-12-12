def count_paths(m, n, blocks):
    """_summary_

    Args:
        m (_type_): _description_
        n (_type_): _description_
        blocks (_type_): _description_

    Returns:
        _type_: _description_
    """
    assert isinstance(m, int) and m > 0
    assert isinstance(n, int) and n > 0
    assert isinstance(blocks, list)
    for b in blocks:
        assert isinstance(b, tuple)
        assert len(b) == 2
        assert isinstance(b[0], int) and isinstance(b[1], int)
        assert -1 < b[0] < m and -1 < b[1] < n

    grids = [['.']*n for _ in range(m)]

    for b in blocks:
        x, y = b
        grids[x][y] = '#'

    dp = [[0]*n for _ in range(m)]
    
    for i in range(len(dp[0])):
        if grids[0][i]!="#":
            dp[0][i]=1
        else:
            break
    
    for i in range(len(dp)):
        if grids[i][0]!="#":
            dp[i][0]=1
        else:
            break
        

    for i in range(1, len(dp)):
        for j in range(1, len(dp[0])):
            if grids[i][j] == '#':
                continue
            left, up = 0, 0
            if grids[i][j-1] != "#":
                left = dp[i][j-1]
            if grids[i-1][j] != "#":
                up = dp[i-1][j]
            dp[i][j] = left+up
    return dp[-1][-1]


if __name__ == "__main__":
    print(count_paths(30, 40, [(0, 3), (1, 1)]))
