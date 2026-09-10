from copy import deepcopy

from matrix_operations import mat_vec_mul


def lu_decompose(a: list[list[float]]) -> tuple[list[list[float]], list[list[float]], list[list[float]], int]:
    n = len(a)
    u = deepcopy(a)
    l = [[1.0 if i == j else 0.0 for j in range(n)] for i in range(n)]
    p = [[1.0 if i == j else 0.0 for j in range(n)] for i in range(n)]

    swaps = 0

    for i in range(n):
        pivot = abs(u[i][i])
        pivot_row = i
        for k in range(i + 1, n):
            if abs(u[k][i]) > pivot:
                pivot = abs(u[k][i])
                pivot_row = k

        if i != pivot_row:
            u[i], u[pivot_row] = u[pivot_row], u[i]
            p[i], p[pivot_row] = p[pivot_row], p[i]
            swaps += 1

            for col in range(i):
                l[i][col], l[pivot_row][col] = l[pivot_row][col], l[i][col]

        for j in range(i + 1, n):
            li = u[j][i] / u[i][i]
            l[j][i] = li
            for col in range(i, n):
                u[j][col] -= li * u[i][col]

    return (l, u, p, swaps)


def forward_substitution(a: list[list[float]], b: list[float]) -> list[float]:
    x: list[float] = []
    for i in range(len(a)):
        xi = b[i]
        for col in range(i):
            xi -= a[i][col] * x[col]
        x.append(xi / a[i][i])
    return x


def backward_substitution(a: list[list[float]], b: list[float]) -> list[float]:
    x = [0.0 for _ in range(len(a))]
    for i in range(len(a) - 1, -1, -1):
        xi = b[i]
        for col in range(len(a) - 1, i - 1, -1):
            xi -= a[i][col] * x[col]
        x[i] = xi / a[i][i]
    return x


def lu_solve(l: list[list[float]], u: list[list[float]], p: list[list[float]], b: list[float]) -> list[float]:
    # LUx = Pb
    # Lz = Pb
    z = forward_substitution(l, mat_vec_mul(p, b))
    # Ux = z
    x = backward_substitution(u, z)
    return x


def calc_det(a: list[list[float]], swaps: int) -> float:
    det = (-1) ** swaps
    for i in range(len(a)):
        det *= a[i][i]
    return det


def lu_inverse(l: list[list[float]], u: list[list[float]], p: list[list[float]]) -> list[list[float]]:
    n = len(l)
    inv_matrix = [[0.0 for _ in range(n)] for _ in range(n)]
    for i in range(n):
        e = [1.0 if i == j else 0.0 for j in range(n)]
        # Ax = e
        x = lu_solve(l, u, p, e)
        for j in range(n):
            inv_matrix[j][i] = x[j]
    return inv_matrix
