from PyQt5.Qt import *
import sys
# 1. 创建一个对象
app = QApplication(sys.argv)

# 2. 控件的操作
# 2.1 创建控件
# 重写mouseMoveEvent
class Mywindow(QWidget):    # 继承Qwidget
    def mouseMoveEvent(self, me):
        QMouseEvent
        # print("鼠标移动了", me.globalPos)
        print("鼠标移动了", me.localPos)
window = Mywindow()
# 2.2 设置控件
window.setWindowTitle("")
window.resize(500, 500)
window.setMouseTracking(True)   # 设置鼠标跟踪
# 2.3 展示控件
window.show()
# 3. 应用程序的执行
sys.exit(app.exec())