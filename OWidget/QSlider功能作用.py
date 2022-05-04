# 封装的类--功能部分
from PyQt5.Qt import *

class Window(QWidget):
    def __init__(self):
        super().__init__()
        QShortcut(QKeySequence(self.tr("Ctrl+W")), self, self.close)
        self.setWindowTitle("QSlider功能")
        self.resize(500, 500)
        self.setup_ui()

    def setup_ui(self):
        label = QLabel("0", self)
        label.move(250, 250)

        sd = QSlider(self)
        sd.move(200, 200)
        sd.setMaximum(100)
        # 设置刻度
        sd.setTickPosition(1)

        # 调节刻度密度
        # sd.setPageStep(10)
        sd.setTickInterval(10)


        def disvalue():
            val = sd.value()
            label.setText(str(val))
            label.adjustSize()
        sd.valueChanged.connect(disvalue)




if __name__ == '__main__':
    import sys
    app = QApplication(sys.argv)
    window = Window()
    window.show()
    sys.exit(app.exec())