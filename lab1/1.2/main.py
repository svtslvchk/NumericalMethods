import numpy as np

from io_utils import read_file, print_vector
from tridiagonal_solver import solve_tridiagonal


if __name__ == "__main__":
    f = input('Введите файл: ')
    a, b, c, d = read_file(f)
    p, q, x = solve_tridiagonal(a, b, c, d)
    print_vector(p, 'p')
    print_vector(q, 'q')
    print_vector(x, 'x')
