from io_utils import read_file, print_matrix, print_vector
from jacobi_solver import jacobi_rotations
from matrix_operations import matmul, is_equal

if __name__ == "__main__":
    a, eps = read_file(input('Введите имя файла: '))
    n = len(a)
    print(f'eps = {eps:.4f}')
    try:
        lambdas, v, iters = jacobi_rotations(a, eps)
        print(f'Количество итераций: {iters}')
        print_vector(lambdas, 'λ')
        print_matrix(v, 'v')
        L = [[lambdas[j] if i == j else 0.0 for j in range(n)] for i in range(n)]
        print_matrix(L, 'L')
        av = matmul(a, v)
        vl = matmul(v, L)
        print_matrix(av, 'AV')
        print_matrix(vl, 'VΛ')
        print(f'AV {'=' if is_equal(av, vl) else '!='} VΛ')
    except RuntimeError as e:
        print(e)
