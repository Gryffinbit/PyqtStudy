from PyQt5.Qt import *
import sys
# 1. 创建一个对象
app = QApplication(sys.argv)

# 2. 控件的操作
# 2.1 创建控件
window = QWidget()
# 2.2 设置控件
window.setWindowTitle("多选按钮")
window.resize(500, 500)

cb = QCheckBox("Python", window)
cb.move(100, 100)
cb.setIcon(QIcon("../../心心相印.png"))
cb.setIconSize(QSize(60, 60))
# 设置是否三态， 没有选中、部分选中、真的被选中
cb.setTristate(True)
# 设置复选框状态
# cb.setCheckState(Qt.PartiallyChecked)  # 部分选中的状态
# cb.setCheckState(Qt.Checked)   # 选中
cb.setCheckState(Qt.Unchecked)   # 未选中

# 监听三态变化
cb.stateChanged.connect(lambda state: print(state))
# 监听两态变化
cb.toggled.connect(lambda isChecked: print(isChecked))


# 2.3 展示控件
window.show()
# 3. 应用程序的执行
sys.exit(app.exec())