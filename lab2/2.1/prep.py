import numpy as np
import matplotlib.pyplot as plt


def y1(x: np.ndarray) -> np.ndarray:
    return np.tan(x) + 1


def y2(x: np.ndarray) -> np.ndarray:
    return 5 * (x ** 2)


def main() -> None:
    # Отрезок для положительной области
    x = np.linspace(0.0, 0.9, 500)

    plt.figure(figsize=(8, 6))
    
    # Строим две функции
    plt.plot(x, y1(x), label=r'$y_1 = \mathrm{tg}(x) + 1$', color='blue', linewidth=2)
    plt.plot(x, y2(x), label=r'$y_2 = 5x^2$', color='red', linewidth=2)

    # Пунктир до точки пересечения (примерно x* ≈ 0.57)
    x_star = 0.5736
    y_star = 5 * (x_star ** 2)
    
    plt.vlines(x=x_star, ymin=0, ymax=y_star, colors='gray', linestyles='--')
    plt.hlines(y=y_star, xmin=0, xmax=x_star, colors='gray', linestyles='--')
    plt.plot(x_star, y_star, 'ro') # Точка пересечения

    # Подписи как в методичке
    plt.text(x_star - 0.03, -0.2, r'$x^*$', fontsize=12)
    
    # Оформление осей
    plt.axhline(0, color='black', linewidth=1)
    plt.axvline(0, color='black', linewidth=1)
    plt.xlim(-0.05, 0.9)
    plt.ylim(-0.3, 4.0)

    plt.title(r'Графическая локализация корня: $\mathrm{tg}(x) + 1 = 5x^2$')
    plt.xlabel('x')
    plt.ylabel('y')
    plt.grid(True, linestyle='--', alpha=0.5)
    plt.legend(loc='upper left')

    plt.tight_layout()
    plt.savefig('root_localization.png', dpi=300)
    print("График пересечения двух функций сохранен в root_localization.png")
    plt.show()


if __name__ == '__main__':
    main()