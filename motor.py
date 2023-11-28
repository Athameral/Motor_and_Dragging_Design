from math import pi
import numpy as np


class Motor:
    """参数具体含义见readme"""

    def __init__(
        self, E_10: float, R_20: float, T_e0: float, I_10: float, T_f: float, n_N: float
    ) -> None:
        """电机参数类

        Args:
            E_10 (float): 额定电动势
            R_20 (float): 额定励磁电阻
            T_e0 (float): 额定转矩
            I_10 (float): 额定电流
            T_f  (float): 摩擦转矩
            n_N  (float): 额定转速(r/min)
        """
        self.E_10 = E_10
        self.R_20 = R_20
        self.T_e0 = T_e0
        self.I_10 = I_10
        self.T_f = 0  # T_f，但是就这样吧
        self.n_N = n_N


# 题目2-18同款参数，作为一个默认电机
Default_Motor = Motor(210, 181.5, 58.616, 87.69, 4.503, 3000)
"""
题目2-18同款参数，作为一个默认电机
"""


def calc_args(
    R1: float, R2: float, U: float, R_L: float, Motor: Motor | None = Default_Motor
) -> tuple[tuple[float, float, float], float, float, float, float, float]:
    """计算需要展示的参数

    Args:
        R1 (float): 调速电阻
        R2 (float): 弱磁电阻
        U (float): 设定电压
        Motor (Motor): 电机参数

    Returns:
        tuple[tuple[float, float, float], float, float, float, float, float]:
        分别为：电功率、电磁功率、机械功率；电动势；电流；转速；电磁转矩；效率
    """
    k_phi = Motor.R_20 / R2
    n = k_phi * Motor.T_e0 * U / R1 - 2 * Motor.T_f * Motor.I_10
    tmp = (
        k_phi**2 * Motor.T_e0 * Motor.E_10 / R1
        + k_phi**2 * Motor.T_e0 * Motor.E_10 / R_L
    )
    n = n / tmp * Motor.n_N
    # 计算原理如果我有空就写到readme里
    # 至此转速已确定
    I_1 = (U - Motor.E_10 * k_phi * n / Motor.n_N) / R1
    # 电流已确定，后续顺理成章
    E_1 = U - I_1 * R1
    T_e = k_phi * I_1 / Motor.I_10 * Motor.T_e0
    P_1 = U * (I_1 + U / R2)
    P_e = T_e * n * 2 * pi / 60
    P_2 = (T_e - Motor.T_f) * n * 2 * pi / 60
    eta = P_2 / P_1
    return (P_1, P_e, P_2, E_1, I_1, n, T_e, eta)


calc_args_2 = np.vectorize(calc_args, excluded=[0, 1, 2])

if __name__ == "__main__":
    print(calc_args(0.2, 200, 220, 5))
    import numpy as np
    import matplotlib.pyplot as plt

    calc2 = np.vectorize(calc_args, excluded=[0, 1, 2])
    rl = np.linspace(100, 1, 1000)
    arr = calc2(0.2, 200, 220, rl)
    arr1 = np.asmatrix(arr)
    plt.plot(rl, arr[5])
    plt.show()
