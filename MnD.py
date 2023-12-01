from threading import Thread, Lock

import numpy as np
from PySide6.QtWidgets import QApplication, QWidget

from Main_Window import Ui_MainUI
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

R1_range = (0.01, 3.0)
R2_range = (15.0, 500.0)
U_range = (50.0, 500.0)


def get_params_and_draw_figures():
    global R1, R2, U
    try:
        R1 = float(ui.LineEdit_R1.text())
        R2 = float(ui.LineEdit_R2.text())
        U = float(ui.LineEdit_U.text())

        draw_8figures()
    except ValueError:
        pass


ui.LineEdit_R1.textChanged.connect(get_params_and_draw_figures)
ui.LineEdit_R2.textChanged.connect(get_params_and_draw_figures)
ui.LineEdit_U.textChanged.connect(get_params_and_draw_figures)


def change_param_texts():
    global R1, R2, U
    R1 = R1_range[0] + ui.Slider_R1.value() / ui.Slider_R1.maximum() * (R1_range[1] - R1_range[0])
    R2 = R2_range[0] + ui.Slider_R2.value() / ui.Slider_R2.maximum() * (R2_range[1] - R2_range[0])
    U = U_range[0] + ui.Slider_U.value() / ui.Slider_U.maximum() * (U_range[1] - U_range[0])

    ui.LineEdit_R1.setText("%.2f" % R1)
    ui.LineEdit_R2.setText("%.2f" % R2)
    ui.LineEdit_U.setText("%.2f" % U)


ui.Slider_R1.valueChanged.connect(change_param_texts)
ui.Slider_R2.valueChanged.connect(change_param_texts)
ui.Slider_U.valueChanged.connect(change_param_texts)
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

for canvas in canvas_list:
    canvas.ax.grid()

canvas_E.ax.set_title("E")
canvas_I.ax.set_title("I")
canvas_I.ax.set_title("I")
canvas_n.ax.set_title("n")
canvas_T.ax.set_title("T")
canvas_eta.ax.set_title("eta")

figure_drawing = False


# 一般来说，绘制很快，200ms左右就可以绘制完成
# 当触发频率不太高时，不用自旋锁也没有什么问题
# 但是在某些场景下，比如拖动滑动条时，触发会非常密集
# 浪费资源且不说，这时一张图上会出现多条曲线，非常恐怖，兄弟。XD
def draw_figure():
    global figure_drawing
    if figure_drawing:
        return
    figure_drawing = True
    if not R1 or not R2 or not U:
        return
    R_L = np.linspace(1, 100, 1000)
    result: tuple[np.ndarray] = calc_args_2(R1, R2, U, R_L)  # (8,1000)

    for canvas in canvas_list:
        for line in canvas.ax.get_lines():
            line.remove()

    canvas_Power.ax.plot(R_L, result[0], label="P1", color="#435c0e")
    canvas_Power.ax.plot(R_L, result[1], label="Pe", color="#008e9f")
    canvas_Power.ax.plot(R_L, result[2], label="P2", color="#9199ff")
    canvas_Power.ax.legend()

    canvas_E.ax.plot(R_L, result[3],color="#136f37")
    canvas_I.ax.plot(R_L, result[4],color="#008068")
    canvas_n.ax.plot(R_L, result[5],color="#008e9f")
    canvas_T.ax.plot(R_L, result[6],color="#0098d1")
    canvas_eta.ax.plot(R_L, result[7],color="#009cf4")

    # TO DO:
    # 保存Line2D对象，避免重复新建对象，以改进颜色变化问题

    for canvas in canvas_list:
        canvas.draw()  # canvas并不会自动更新
    # 绘制结束
    figure_drawing = False


def draw_8figures():
    global figure_drawing
    if figure_drawing:
        return
    thread = Thread(target=draw_figure)
    thread.start()


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

switch_figure()
app.exec()
