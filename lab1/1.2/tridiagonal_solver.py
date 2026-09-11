def check_strict_diagonal_dominance(a: list[float], b: list[float], c: list[float]) -> bool:
    if not (abs(b[0]) >= abs(a[0]) + abs(c[0])):
        return False
    for i in range(1, len(a) - 1):
        if not (abs(b[i]) >= abs(a[i]) + abs(c[i])):
            return False
        if a[i] == 0 or c[i] == 0:
            return False
    if a[len(a) - 1] == 0 or c[len(a) - 1] == 0:
        return False
    return True


def solve_tridiagonal(a: list[float], b: list[float], c: list[float], d: list[float]) -> tuple[list[float], list[float], list[float]]:
    n = len(a)
    p = [0.0] * n
    q = [0.0] * n
    p[0] = -b[0] / c[0]
    p[n - 1] = 0
    q[0] = d[0] / b[0]
    for i in range(1, n - 1):
        p[i] = -c[i] / (b[i] + a[i] * p[i - 1])
        q[i] = (d[i] - a[i] * q[i - 1]) / (b[i] + a[i] * p[i - 1])
    q[n - 1] = (d[n - 1] - a[n - 1] * q[n - 2]) / (b[n - 1] + a[n - 1] * p[n - 2])

    x = [0.0] * n
    x[n - 1] = q[n - 1]
    for i in range(n - 2, -1, -1):
        x[i] = p[i] * x[i + 1] + q[i]
    return p, q, x
