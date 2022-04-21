from PyQt5.Qt import *
import sys
# 1. 创建一个对象
app = QApplication(sys.argv)

# 2. 控件的操作
# 2.1 创建控件
# 组合窗口（有标题栏、状态栏等，组合起来的）
window = QMainWindow()
# 采用懒加载的方式，用到的时候才会创建
window.statusBar()    # 状态栏
# window = QWidget()
# 2.2 设置控件
window.setWindowTitle("信息提示案例")
window.resize(500, 500)
window.setWindowFlag(Qt.WindowContextHelpButtonHint)

# 设置信息提示
window.setStatusTip("这是窗口")
# 获取信息提示
print(window.statusTip())

label = QLabel(window)
label.setText("hello")
label.setStatusTip("这是你好")
label.setToolTip("这是一个提示标签")
label.setWhatsThis("这是一个标签")
print(label.toolTip())
# 设置展示时间
label.setToolTipDuration(2000)   # 单位是毫秒
# 2.3 展示控件
window.show()
# 3. 应用程序的执行
sys.exit(app.exec())