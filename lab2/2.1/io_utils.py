def print_iteration_table(method_name: str, history: list[tuple[int, float, float]]) -> None:
    print(f"\n{'=' * 55}")
    print(f"   {method_name}")
    print(f"{'=' * 55}")
    print(f"{'Итерация':^14}|{'x^(k)':^20}|{'Погрешность':^20}")
    print(f"{'-' * 14}+{'-' * 20}+{'-' * 20}")

    for k, x_k, error in history:
        err_str = f"{error:^22.8e}" if error is not None else f"{'—':^22}"
        print(f"{k:^14d}|{x_k:^20.8f}|{err_str}")

    final_k, final_x, _ = history[-1]
    print(f"{'-' * 55}")
    print(f"Результат: x* = {final_x:.8f} (найден за {final_k} итераций)\n")