import math
from copy import deepcopy
from typing import Union

from matrix_operations import matmul, outer_product, vector_norm, norm_subdiagonal



def householder_reflection(a: list[list[float]], k: int) -> list[list[float]]:
    n = len(a)
    sub_col = [a[j][k] for j in range(k, n)]
    sub_norm = vector_norm(sub_col)
    v = [0.0 for _ in range(n)]
    sign = 1.0 if a[k][k] >= 0 else -1.0
    v[k] = a[k][k] + sign * sub_norm
    for j in range(k + 1, n):
        v[j] = a[j][k]
    vtv = vector_norm(v) ** 2
    vvt = outer_product(v, v)
    h = [[0.0 for _ in range(n)] for _ in range(n)]
    for i in range(n):
        for j in range(n):
            delta = 1.0 if i == j else 0.0
            h[i][j] = delta - 2.0 * (vvt[i][j] / vtv)
    return h


def qr_decomposition(a: list[list[float]]) -> tuple[list[list[float]], list[list[float]]]:
    n = len(a)
    r = deepcopy(a)
    q = [[1.0 if i == j else 0.0 for j in range(n)] for i in range(n)]
    for k in range(n - 1):
        hk = householder_reflection(r, k)
        r = matmul(hk, r)
        q = matmul(q, hk)
    return q, r


def extract_eigenvalues(a: list[list[float]], eps: float) -> list[Union[float, complex]]:
    n = len(a)
    eigenvalues: list[Union[float, complex]] = []
    i = 0
    while i < n:
        if i == n - 1:
            eigenvalues.append(a[i][i])
            i += 1
        elif abs(a[i + 1][i]) <= eps:
            eigenvalues.append(a[i][i])
            i += 1
        else:
            trace = a[i][i] + a[i + 1][i + 1]
            det = a[i][i] * a[i + 1][i + 1] - a[i][i + 1] * a[i + 1][i]
            disc = trace ** 2 - 4.0 * det
            if disc >= 0:
                l1 = (trace + math.sqrt(disc)) / 2.0
                l2 = (trace - math.sqrt(disc)) / 2.0
                eigenvalues.extend([l1, l2])
            else:
                re = trace / 2.0
                im = math.sqrt(abs(disc)) / 2.0
                eigenvalues.append(complex(re, im))
                eigenvalues.append(complex(re, -im))
            i += 2
    return eigenvalues


def qr_alg(
        a: list[list[float]], eps: float, max_iters: int = 1000
) -> tuple[list[Union[float | complex]], list[list[float]], int]:
    ak = deepcopy(a)
    for it in range(1, max_iters + 1):
        q, r = qr_decomposition(ak)
        ak = matmul(r, q)
        if norm_subdiagonal(ak) <= eps:
            return extract_eigenvalues(ak, eps), ak, it
    raise RuntimeError(
        f'Алгоритм не сошелся за {max_iters} итераций.'
    )
