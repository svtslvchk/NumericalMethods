from iter_utils import matrix_norm, diff_vectors_norm


def solve_simple_iteration(
        alpha: list[list[float]],
        beta: list[float],
        eps: float,
        max_iters: int = 1000
) -> tuple[list[float], int]:
    n = len(alpha)
    norm_alpha = matrix_norm(alpha)
    factor = norm_alpha / (1 - norm_alpha)

    x1 = list(beta)
    x2 = [0.0 for _ in range(n)]
    for k in range(max_iters):
        for i in range(n):
            s = sum(alpha[i][j] * x1[j] for j in range(n))
            x2[i] = beta[i] + s

        diff = diff_vectors_norm(x2, x1)
        eps_k = factor * diff
        if eps_k <= eps:
            return x2, k
        x1 = list(x2)
    raise RuntimeError(f'МПИ не сошелся за {max_iters} итераций.')


def solve_seidel(
        alpha: list[list[float]],
        beta: list[float],
        eps: float,
        max_iters: int = 1000
) -> tuple[list[float], int]:
    n = len(alpha)
    norm_alpha = matrix_norm(alpha)
    factor = norm_alpha / (1 - norm_alpha)

    x = list(beta)
    for k in range(max_iters):
        x1 = list(x)
        for i in range(n):
            s = sum(alpha[i][j] * x[j] for j in range(n))
            x[i] = beta[i] + s

        diff = diff_vectors_norm(x, x1)
        eps_k = factor * diff
        if eps_k <= eps:
            return x, k
    raise RuntimeError(f'Метод Зейделя не сошелся за {max_iters} итераций.')
