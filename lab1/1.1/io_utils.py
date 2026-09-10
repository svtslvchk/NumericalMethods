def read_file(filename: str) -> tuple[list[list[float]], list[float]]:
    with open(filename, 'r') as f:
        lines = [line.strip() for line in f if line.strip()]
    A = [[0.0 for _ in range(len(lines))] for _ in range(len(lines))]
    b = [0.0 for _ in range(len(lines))]
    for i, line in enumerate(lines):
        left, right = line.split('=')
        b[i] = float(right.strip())
        terms = parse_left_part(left)
        terms_sort = sorted(terms, key=lambda x: x[1])
        for coeff, idx in terms_sort:
            A[i][idx - 1] = coeff
    return A, b


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


def print_matrix(matrix: list[list[float]], name: str = "", precision: int = 4) -> None:
    if name:
        print(f"=== {name} ===")

    for row in matrix:
        formatted_row = " ".join(f"{val:10.{precision}f}" for val in row)
        print(f"[ {formatted_row} ]")
    print()
