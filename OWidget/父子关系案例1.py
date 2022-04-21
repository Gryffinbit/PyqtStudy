from PyQt5.Qt import *
import sys
# 1. 创建一个对象
app = QApplication(sys.argv)

class Window(QWidget):
    def mousePressEvent(self, evt):
        local_x = evt.x()
        local_y = evt.y()
        sub_widget = self.childAt(local_x, local_y)
        if sub_widget is not None:
            sub_widget.setStyleSheet("background-color:pink;")
        print("标签被点击了", local_x, local_y)

# 2. 控件的操作
# 2.1 创建控件
window = Window()
# 2.2 设置控件
window.setWindowTitle("")
window.resize(500, 500)

for i in range(1, 11):
    label = QLabel(window)
    label.setText("标签"+  str(i))
    label.move(40*i, 40*i)
# 2.3 展示控件
window.show()
# 3. 应用程序的执行
sys.exit(app.exec())