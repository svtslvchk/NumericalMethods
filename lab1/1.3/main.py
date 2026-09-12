import numpy as np

from io_utils import read_file, print_comparison_results
from iterative_solver import solve_simple_iteration, solve_seidel
from iter_utils import matrix_norm, to_iterative, check_diagonal_dominance


if __name__ == "__main__":
    a, b, eps = read_file(input('Введите имя файла: '))
    alpha, beta = to_iterative(a, b)
    if not check_diagonal_dominance(a):
        print('Матрица не обладает строгим диагональным преобладанием!')

    alpha_norm = matrix_norm(alpha)
    if alpha_norm >= 1.0:
        print(f'alpha = {alpha:.2f}. Достаточное условие сходимости не выполнено.')
    
    x_jacobi, iters_jacobi = solve_simple_iteration(alpha, beta, eps)
    x_seidel, iters_seidel = solve_seidel(alpha, beta, eps)
    x_np = np.linalg.solve(np.array(a), np.array(b)).tolist()
    print_comparison_results(
        eps, iters_jacobi, x_jacobi, iters_seidel, x_seidel, x_np
    )


