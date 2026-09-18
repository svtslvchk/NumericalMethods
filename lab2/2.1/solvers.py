from typing import Callable


def simple_iteration(
    phi: Callable[[float], float], x0: float, eps: float, max_iter: int = 1000
) -> tuple[float, list[tuple[int, float, float]]]:
    history = [(0, x0, None)]
    x = x0

    for k in range(max_iter):
        x1 = phi(x)
        error = abs(x1 - x)
        history.append((k, x, error))

        if error < eps:
            return x1, history

        x = x1

    raise RuntimeError(f"МПИ не сошелся за {max_iter} итераций.")


def newton_method(
    f: Callable[[float], float], df: Callable[[float], float], x0: float,
    eps: float, max_iter: int = 1000
) -> tuple[float, list[tuple[int, float, float]]]:
    history = [(0, x0, None)]
    x = x0

    for k in range(max_iter):
        f_val = f(x)
        df_val = df(x)

        if abs(df_val) < 1e-12:
            raise ZeroDivisionError("Производная близка к нулю! Метод Ньютона остановлен.")

        x1 = x - (f_val / df_val)
        error = abs(x1 - x)
        history.append((k, x, error))

        if error < eps:
            return x1, history

        x = x1

    raise RuntimeError(f"Метод Ньютона не сошелся за {max_iter} итераций.")
