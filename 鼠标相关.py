from PyQt5.Qt import *
import sys
# 1. 创建一个对象
app = QApplication(sys.argv)

# 2. 控件的操作
# 2.1 创建控件
window = QWidget()
# 2.2 设置控件
window.setWindowTitle("鼠标相关操作")
window.resize(500, 500)
# window.setCursor(Qt.SizeVerCursor)

# 在特定范围里设置cursor的样式
# label = QLabel(window)
# label.setText("hello world")
# label.setStyleSheet("background-color:pink;")
# label.setCursor(Qt.ForbiddenCursor)

# 设置鼠标样式-图片
pixmap = QPixmap("OWidget/cursor.jpg")
pixmap = pixmap.scaled(50, 50)
cursor = QCursor(pixmap, 0, 0)
window.setCursor(cursor)
window.unsetCursor()   # 恢复原样

current_cursor = window.cursor()   # 设置鼠标的位置
current_cursor.setPos(100, 100)


# 2.3 展示控件
window.show()
# 3. 应用程序的执行
sys.exit(app.exec())