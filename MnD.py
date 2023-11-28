from PySide6.QtWidgets import QApplication, QWidget, QPushButton
from Main_Window import Ui_MainUI
from threading import Thread

from matplotlib.backends.backend_qtagg import FigureCanvasQTAgg
import numpy as np

from motor import calc_args_2
from mplcanvas import MplCanvas

app = QApplication()

Main_Window = QWidget()
ui = Ui_MainUI()
ui.setupUi(Main_Window)
Main_Window.show()

# 定义需要用户指定的变量，并绑定

R1 = 0.0
R2 = 0.0
U = 0.0


def set_R1():
    global R1
    try:
        R1 = float(ui.LineEdit_R1.text())
    except:
        pass


def set_R2():
    global R2
    try:
        R2 = float(ui.LineEdit_R2.text())
    except:
        pass


def set_U():
    global U
    try:
        U = float(ui.LineEdit_U.text())
    except:
        pass


ui.LineEdit_R1.textEdited.connect(set_R1)
ui.LineEdit_R2.textEdited.connect(set_R2)
ui.LineEdit_U.textEdited.connect(set_U)

# button = QPushButton(parent=Main_Window)
# button.show()


# def testslot():
#     print(calc_args(R1, R2, U, 50))


# button.clicked.connect(testslot)

# 选择绘制类型

figure_type = ("功率", "电动势", "电流", "转速", "转矩", "效率")
ui.Figure_SelectBox.addItems(figure_type)

# 定义绘制函数
canvas_Power = MplCanvas()
canvas_E = MplCanvas()
canvas_I = MplCanvas()
canvas_n = MplCanvas()
canvas_T = MplCanvas()
canvas_eta = MplCanvas()

canvas_list = (canvas_Power, canvas_E, canvas_I, canvas_n, canvas_T, canvas_eta)


def draw_figure():
    R_L = np.linspace(1, 100, 1000)
    result: tuple[np.ndarray] = calc_args_2(R1, R2, U, R_L)  # (8,1000)

    canvas_Power.ax.clear()
    canvas_E.ax.clear()
    canvas_I.ax.clear()
    canvas_n.ax.clear()
    canvas_T.ax.clear()
    canvas_eta.ax.clear()

    canvas_Power.ax.plot(R_L, result[0], label="P1")
    canvas_Power.ax.plot(R_L, result[1], label="Pe")
    canvas_Power.ax.plot(R_L, result[2], label="P2")
    canvas_Power.ax.legend()

    canvas_E.ax.plot(R_L, result[3])
    canvas_E.ax.set_title("E")
    canvas_E.ax.grid()

    canvas_I.ax.plot(R_L, result[4])
    canvas_I.ax.set_title("I")
    canvas_I.ax.grid()

    canvas_n.ax.plot(R_L, result[5])
    canvas_n.ax.set_title("n")
    canvas_n.ax.grid()

    canvas_T.ax.plot(R_L, result[6])
    canvas_T.ax.set_title("T")
    canvas_T.ax.grid()

    canvas_eta.ax.plot(R_L, result[7])
    canvas_eta.ax.set_title("eta")
    canvas_eta.ax.grid()

    for canva in canvas_list:
        canva.draw()  # canva并不会自动更新
    # 绘制结束
    pass


def draw_8figures():
    thread = Thread(target=draw_figure)
    thread.start()
    pass


def switch_figure():
    item = ui.Figure_Frame_Layout.takeAt(0)
    if item:
        item.widget().setParent(None)
        # 这一句必须加上，否则第二次选择某张图的时候无法再显示了
        # 原因是Pyside6有所有权机制，当添加widget时，会自动设置其parent，如果已经有parent，则不会继续添加。
        # 所以必须先让它变成孤儿（笑），才能再有parent
        ui.Figure_Frame_Layout.removeItem(item)
    ui.Figure_Frame_Layout.addWidget(canvas_list[ui.Figure_SelectBox.currentIndex()])
    pass


# 绑定绘制按钮和ComboBox
ui.Button_Draw.clicked.connect(draw_8figures)
ui.Figure_SelectBox.currentIndexChanged.connect(switch_figure)

app.exec()
