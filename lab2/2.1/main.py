import math
import matplotlib.pyplot as plt
from scipy.optimize import root_scalar

from target_function import f, df, phi
from solvers import simple_iteration, newton_method
from io_utils import print_iteration_table


def plot_convergence(history_mpi, history_newton) -> None:
    # Исключаем шаг k=0, так как на нем погрешности еще нет
    k_mpi = [step[0] for step in history_mpi if step[2] is not None]
    err_mpi = [step[2] for step in history_mpi if step[2] is not None]

    k_newton = [step[0] for step in history_newton if step[2] is not None]
    err_newton = [step[2] for step in history_newton if step[2] is not None]

    plt.figure(figsize=(9, 5))
    plt.semilogy(k_mpi, err_mpi, 'o-', label='Метод простой итерации (МПИ)', color='blue')
    plt.semilogy(k_newton, err_newton, 's-', label='Метод Ньютона', color='red')

    plt.title('Сравнение скорости сходимости методов')
    plt.xlabel('Номер итерации (k)')
    plt.ylabel('Погрешность |x^(k) - x^(k-1)| (log scale)')
    plt.grid(True, which='both', linestyle='--', alpha=0.6)
    max_k = max(max(k_mpi, default=1), max(k_newton, default=1))
    plt.xticks(range(1, max_k + 1))
    plt.legend()
    plt.tight_layout()
    plt.savefig('convergence_plot.png', dpi=300)
    print("График сходимости сохранен в файл convergence_plot.png")
    plt.show()


def main() -> None:    
    eps_input = input("Введите точность eps: ")
    eps = float(eps_input)

    x0_input = input("Введите начальное приближение x0 (по умолчанию 0.8): ")
    x0 = float(x0_input) if x0_input else 0.8

    try:
        root_mpi, history_mpi = simple_iteration(phi, x0, eps)
        print_iteration_table("Метод Простой Итерации (МПИ)", history_mpi)
    except Exception as e:
        print(f"Ошибка при выполнении МПИ: {e}")
        return

    try:
        root_newton, history_newton = newton_method(f, df, x0, eps)
        print_iteration_table("Метод Ньютона", history_newton)
    except Exception as e:
        print(f"Ошибка при выполнении метода Ньютона: {e}")
        return

    res_scipy = root_scalar(f, fprime=df, x0=x0, method='newton')
    print(f"Контрольная проверка (scipy.optimize.root_scalar): x* = {res_scipy.root:.8f}")

    plot_convergence(history_mpi, history_newton)


if __name__ == '__main__':
    main()
