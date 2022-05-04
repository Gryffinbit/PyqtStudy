# 封装的类--功能部分
from PyQt5.Qt import *

class Window(QWidget):
    def __init__(self):
        super().__init__()
        QShortcut(QKeySequence(self.tr("Ctrl+W")), self, self.close)
        self.setWindowTitle("QAbstractSlider")
        self.resize(500, 500)
        self.setup_ui()

    def setup_ui(self):


        QAbstractSlider
        sd = QSlider(self)
        # 设置步长(要键盘按上下才会显示这种步长）
        sd.setSingleStep(5)
        # 滑块数值变化显示
        label = QLabel("0", self)
        label.move(100, 100)

        # QSlider子类特色
        sd.setTickInterval(3)



        # 设置滑块方向
        # sd.setOrientation(Qt.Horizontal)
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