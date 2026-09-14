def read_file(filename: str) -> tuple[list[list[float]], float]:
    with open(filename, 'r') as f:
        lines = [line.strip() for line in f if line.strip()]
    n = len(lines) - 1
    a = [[0.0 for _ in range(n)] for _ in range(n)]
    for i, line in enumerate(lines):
        if i == n:
            continue
        coeffs = list(map(float, line.split()))
        a[i] = coeffs
    return a, float(lines[-1])


def print_matrix(a: list[list[float]], name: str, precision: int = 6) -> None:
    print(f"=========={name.upper()}===========")
    for row in a:
        formatted_row = " ".join(f"{val:10.{precision}f}" for val in row)
        print(f"[ {formatted_row} ]")
    print()


def print_vector(x: list[float], name: str) -> None:
    print(f'=========={name.upper()}==========')
    for i in range(len(x)):
        print(f'{name}{i + 1} = {x[i]}')
