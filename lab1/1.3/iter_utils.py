def matrix_norm(a: list[list[float]]) -> float:
    return max(sum(abs(it) for it in row) for row in a)


def diff_vectors_norm(a: list[float], b: list[float]) -> float:
    return max(abs(x - y) for x, y in zip(a, b))


def check_diagonal_dominance(a: list[list[float]]) -> bool:
    n = len(a)
    for i in range(n):
        s = sum(abs(a[i][j]) for j in range(n) if i != j)
        if abs(a[i][i]) <= s:
            return False
    return True


def to_iterative(a: list[list[float]], b: list[float]) -> tuple[list[list[float]], list[float]]:
    n = len(a)
    alpha = [[0.0 for _ in range(n)] for _ in range(n)]
    beta = [0.0 for _ in range(n)]
    for i in range(n):
        beta[i] = b[i] / a[i][i]
        for j in range(n):
            if i != j:
                alpha[i][j] = -a[i][j] / a[i][i]
    return alpha, beta
