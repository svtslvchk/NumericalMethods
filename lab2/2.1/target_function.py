import math


def f(x: float) -> float:
    return math.tan(x) - 5.0 * (x ** 2) + 1.0


def df(x: float) -> float:
    cos_x = math.cos(x)
    return (1.0 / (cos_x ** 2)) - 10.0 * x


def phi(x: float, lmbda: float = -0.16) -> float:
    return x - lmbda * f(x)
