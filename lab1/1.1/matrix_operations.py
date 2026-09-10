def matmul(x: list[list[float]], y: list[list[float]]) -> list[list[float]]:
    rows_x = len(x)
    cols_x = len(x[0])
    cols_y = len(y[0])
    res = [[0.0 for _ in range(cols_y)] for _ in range(rows_x)]
    for i in range(rows_x):
        for j in range(cols_y):
            for k in range(cols_x):
                res[i][j] += x[i][k] * y[k][j]
    return res


def mat_vec_mul(x: list[list[float]], y: list[float]) -> list[float]:
    res = []
    for row in x:
        r = 0.0
        for i in range(len(row)):
            r += row[i] * y[i]
        res.append(r)
    return res
