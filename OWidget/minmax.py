from PyQt5.Qt import *
import sys
# 1. 创建一个对象
app = QApplication(sys.argv)

# 2. 控件的操作
# 2.1 创建控件
window = QWidget()
# 2.2 设置控件
window.setWindowTitle("最小最大尺寸限定")
# window.resize(500, 500)
window.setMinimumSize(200, 200)
window.setMaximumSize(500, 500)


# 2.3 展示控件
window.show()
# 3. 应用程序的执行
sys.exit(app.exec())