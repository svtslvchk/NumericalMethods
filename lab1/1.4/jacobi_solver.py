import math
from copy import deepcopy

from matrix_operations import transpose, matmul
from io_utils import print_matrix


def is_symmetric(a: list[list[float]], e: float = 1e-9) -> bool:
    n = len(a)
    for i in range(n):
        for j in range(i + 1, n):
            if abs(a[i][j] - a[j][i]) > e:
                return False
    return True


def find_max_off_diag(a: list[list[float]]) -> tuple[int, int, float]:
    n = len(a)
    mx = 0.0
    mx_cord = (0, 0)
    for i in range(n):
        for j in range(i + 1, n):
            if abs(a[i][j]) > mx:
                mx = abs(a[i][j])
                mx_cord = (i, j)
    return (mx_cord[0], mx_cord[1], a[mx_cord[0]][mx_cord[1]])


def off_diag_norm(a: list[list[float]]) -> float:
    s = 0.0
    n = len(a)
    for i in range(n):
        for j in range(i + 1, n):
            s += a[i][j] ** 2
    return (2 * s) ** 0.5


def calc_rotation_angles(a_i: float, a_j: float, a_ij: float) -> tuple[float, float]:
    if abs(a_i - a_j) < 1e-9:
        phi = math.pi / 4
        return (math.cos(phi), math.sin(phi))

    phi = 0.5 * math.atan(2 * a_ij / (a_i - a_j))
    return math.cos(phi), math.sin(phi)


def create_rotation_matrix(x: int, y: int, c: float, s: float, n: int) -> list[list[float]]:
    u = [[1.0 if i == j else 0.0 for j in range(n)] for i in range(n)]
    u[x][x] = c
    u[x][y] = -s
    u[y][x] = s
    u[y][y] = c
    return u


def jacobi_rotations(
        a: list[list[float]], eps: float, max_iters: int = 100
) -> tuple[list[float], list[list[float]], int]:
    if not is_symmetric(a):
        raise ValueError(
            'Матричца должна быть симметричной.'
        )

    n = len(a)
    A = deepcopy(a)
    v = [[1.0 if i == j else 0.0 for j in range(n)] for i in range(n)]
    for it in range(1, max_iters + 1):
        if off_diag_norm(A) <= eps:
            return [A[i][i] for i in range(n)], v, it - 1

        x, y, a_xy = find_max_off_diag(A)
        c, s = calc_rotation_angles(A[x][x], A[y][y], a_xy)
        u = create_rotation_matrix(x, y, c, s, n)
        u_t = transpose(u)
        A = matmul(matmul(u_t, A), u)
        v = matmul(v, u)
    raise RuntimeError(
        f'Алгоритм не сошелся за {max_iters} итераций.'
    )
