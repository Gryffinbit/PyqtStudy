from PyQt5.Qt import *
import sys
# 1. 创建一个对象
app = QApplication(sys.argv)

# 2. 控件的操作
# 2.1 创建控件
window = QWidget()
# 2.2 设置控件
window.setWindowTitle("单选操作")
window.resize(500, 500)

rb_nan = QRadioButton(window)
rb_nan.move(100, 100)
rb_nan.setText("男")
# 设置快捷键
rb_nan.setShortcut("Meta+M")
# 设置默认选项
rb_nan.setChecked(True)

rb_nv = QRadioButton(window)
rb_nan.move(100, 150)
rb_nv.setText("女-&Female")



# 2.3 展示控件
window.show()
# 3. 应用程序的执行
sys.exit(app.exec())