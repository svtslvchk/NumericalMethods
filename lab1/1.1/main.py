import numpy as np

from io_utils import read_file, print_matrix
from matrix_operations import matmul
from lu import lu_inverse, lu_solve, lu_decompose, calc_det


if __name__ == "__main__":
    filename = input()
    a, b = read_file(filename)
    l, u, p, swaps = lu_decompose(a)
    print('==========L==========')
    print_matrix(l)
    print('==========U==========')
    print_matrix(u)
    print('==========LU==========')
    print_matrix(matmul(l, u))
    x = lu_solve(l, u, p, b)
    print('==========X==========')
    for i in range(len(x)):
        print(f'x{i + 1} = {x[i]}')
    print('==========INVERSE A==========')
    inverse_a = lu_inverse(l, u, p)
    print_matrix(inverse_a)
    print('==========detA==========')
    print(calc_det(u, swaps))
    print('==========AA^-1==========')
    print_matrix(matmul(a, inverse_a))
    print('==========LU==========')
    print_matrix(matmul(l, u))
    print('==========PA==========')
    print_matrix(matmul(p, a))

    a_np = np.array(a)
    b_np = np.array(b)

    x_np = np.linalg.solve(a_np, b_np)
    det_np = np.linalg.det(a_np)
    inv_np = np.linalg.inv(a_np)

    print('==========NUMPY CHECK==========')
    print(f"x (NumPy): {x_np}")
    print(f"det(A) (NumPy): {det_np:.4f}")
    print("A^-1 (NumPy):")
    print(inv_np)
