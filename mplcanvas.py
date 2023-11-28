from matplotlib.backends.backend_qtagg import FigureCanvasQTAgg
from matplotlib.figure import Figure

class MplCanvas(FigureCanvasQTAgg):
    def __init__(self, width : float | None = 4, height : float | None = 4) -> None:
        fig = Figure(figsize=(width,height))
        self.ax = fig.add_subplot()
        super().__init__(fig)

