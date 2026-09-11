def read_file(filename: str) -> tuple[list[float], list[float], list[float], list[float]]:
    with open(filename, 'r') as f:
        lines = [line.strip() for line in f if line.strip()]

    n = len(lines)
    a = [0.0] * n
    b = [0.0] * n
    c = [0.0] * n
    d = [0.0] * n

    for i, line in enumerate(lines):
        left, right = line.split('=')
        d[i] = float(right.strip())

        terms = parse_left_part(left)

        for coeff, idx in terms:
            var_idx = idx - 1

            if var_idx == i:
                b[i] = coeff
            elif var_idx == i - 1:
                a[i] = coeff
            elif var_idx == i + 1:
                c[i] = coeff

    return a, b, c, d


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
