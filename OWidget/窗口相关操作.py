from PyQt5.Qt import *
from PyQt5.QtGui import QIcon
import sys
class Window(QWidget):
    def mousePressEvent(self, QMouseEvent):

        if self.isMaximized():
            self.setWindowState(Qt.WindowNoState)
            # self.showNormal()
        else:
            self.setWindowState(Qt.WindowMaximized)
            # self.showMaximized()
# 1. 创建一个对象
app = QApplication(sys.argv)

# 2. 控件的操作
# 2.1 创建控件
window = Window()
# window = QWidget()
# 2.2 设置控件

window.resize(500, 500)

icon = QIcon("../心心相印.svg")   #  QIcon(str)  str 是图标的路径

app.setWindowIcon(icon)



window.setWindowOpacity(1.0 )
print(window.windowOpacity())

# 使窗口始终保持在最上面
window.setWindowFlag(Qt.WindowStaysOnTopHint)
# 设置初始状态
# window.setWindowState(Qt.WindowMinimized)  ## 最小化
# window.setWindowState(Qt.WindowFullScreen)  ## 全屏
# window.setWindowState(Qt.WindowMaximized)   #最大化

# 2.3 展示控件
window.show()
window.showMinimized()
# window.showMaximized()  展示最大化
# 3. 应用程序的执行
sys.exit(app.exec())