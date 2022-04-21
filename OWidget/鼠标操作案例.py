import sys
from PyQt5.Qt import *
# 要求：鼠标移入窗口时，让label位置跟随鼠标位置；让鼠标设置为指定图标
class Window(QWidget):
    def mouseMoveEvent(self, mv):
        print("鼠标移动", mv.localPos())
        label = self.findChildren(QLabel)    # 在父控件里查找子控件，因为label在下面的子控件里
        label.move(mv().x(), mv().y())
app = QApplication(sys.argv)

window = Window()
window.resize(500, 500)
window.setWindowTitle("鼠标相关案例")
window.move(200, 200)

pixmap = QPixmap("OWidget/cursor.jpg").scaled(50, 50)

cursor = QCursor(pixmap)
window.setCursor(cursor)

label = QLabel(window)
label.setText("hello world")
label.move(100, 100)
label.setStyleSheet("background-color:pink;")

window.setMouseTracking(True)     # 开启鼠标跟踪

window.show()

sys.exit(app.exec())