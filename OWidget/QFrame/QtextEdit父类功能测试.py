from PyQt5.Qt import *
import sys

# 1. 创建一个对象
app = QApplication(sys.argv)

# 2. 控件的操作
# 2.1 创建控件
window = QWidget()
# 2.2 设置控件
window.setWindowTitle("QWidge是他的父类")
window.resize(500, 500)

te = QTextEdit("狗屎", window)
te.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOn)


# 设置角落控件

# btn = QPushButton(window)
# btn.setIcon(QIcon("../../心心相印.png"))
# te.setCornerWidget(btn)

# QTextedit支持Html标签样式

# 2.3 展示控件
QShortcut(QKeySequence(window.tr("Ctrl+W")), window, window.close)
window.show()
# 3. 应用程序的执行
sys.exit(app.exec())