def read_file(filename: str) -> tuple[list[list[float]], list[float], float]:
    with open(filename, 'r') as f:
        lines = [line.strip() for line in f if line.strip()]

    n = len(lines) - 1
    A = [[0.0 for _ in range(n)] for _ in range(n)]
    b = [0.0 for _ in range(n)]
    for i, line in enumerate(lines):
        if i == len(lines) - 1:
            eps = float(line)
            continue
        left, right = line.split('=')
        b[i] = float(right.strip())
        terms = parse_left_part(left)
        terms_sort = sorted(terms, key=lambda x: x[1])
        for coeff, idx in terms_sort:
            A[i][idx - 1] = coeff
    return A, b, eps


def parse_left_part(s: str) -> list[tuple[float, int]]:
    s = s.replace('-', '+-')
    terms = [x.strip() for x in s.split('+') if x.strip()]
    res = []
    for term in terms:
        coeff, idx = term.split('x')
        coeff = coeff.replace(' ', '')
        if coeff in ('', '+'):
            coeff_val = 1.0
        elif coeff == '-':
            coeff_val = -1.0
        else:
            coeff_val = float(coeff)
        res.append((coeff_val, int(idx)))
    return res


def print_vector(x: list[float], name: str) -> None:
    print(f'=========={name.upper()}==========')
    for i in range(len(x)):
        print(f'{name}{i + 1} = {x[i]}')


def print_comparison_results(
    eps: float,
    iter_jacobi: int,
    x_jacobi: list[float],
    iter_seidel: int,
    x_seidel: list[float],
    x_numpy: list[float]
) -> None:
    print("==================================================")
    print(f"Заданная точность (eps): {eps}")
    print("==================================================\n")

    print(f"--- 1. Метод простых итераций (Якоби) ---")
    print(f"Количество итераций: {iter_jacobi}")
    print_vector(x_jacobi, name="x")

    print(f"--- 2. Метод Зейделя ---")
    print(f"Количество итераций: {iter_seidel}")
    print_vector(x_seidel, name="x")

    print(f"--- 3. Эталонное решение (NumPy) ---")
    print_vector(x_numpy, name="x_np")

    print("================ СРАВНЕНИЕ СКОРОСТИ ==============")
    if iter_seidel < iter_jacobi:
        diff = iter_jacobi - iter_seidel
        print(f"Метод Зейделя сошелся быстрее на {diff} итераций.")
    elif iter_seidel == iter_jacobi:
        print("Оба метода сошлись за одинаковое количество итераций.")
    else:
        print("Метод простых итераций сошелся быстрее.")
    print("==================================================")