import numpy as np

from io_utils import read_file, print_matrix, print_eigenvalues
from qr_solver import qr_decomposition, qr_alg
from matrix_operations import matmul, is_equal


if __name__ == "__main__":
    a, eps = read_file(input('Введите имя файла: '))
    print_matrix(a, 'a')
    q1, r1 = qr_decomposition(a)
    print('Q и R на шаге 1:')
    print_matrix(q1, 'q')
    print_matrix(r1, 'r')
    qr = matmul(q1, r1)
    print_matrix(qr, 'QR')
    print(f'A {'=' if is_equal(qr, a) else '!='} QR')
    try:
        eigenvalues, A, iters = qr_alg(a, eps)
        print(f'Количество итераций: {iters}')
        print('Финальная матрица:')
        print_matrix(A, 'A')
        print_eigenvalues(eigenvalues)
        a_np = np.array(A, dtype=float)
        eigenvalues_np, _ = np.linalg.eig(a_np)
        print('Эталонные собственные значения (NumPy)')
        print_eigenvalues(list(eigenvalues_np))
    except RuntimeError as e:
        print(e)
