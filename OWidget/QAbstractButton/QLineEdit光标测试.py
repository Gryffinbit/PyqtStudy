from PyQt5.Qt import *
import sys

# 1. 创建一个对象
app = QApplication(sys.argv)

# 2. 控件的操作
# 2.1 创建控件
window = QWidget()
# 2.2 设置控件
window.setWindowTitle("光标功能测试")
window.resize(500, 500)


le = QLineEdit(window)
le.move(100, 100)

btn = QPushButton("button", window)
btn.move(50, 50)
# def cursor_move():
#     # le.cursorBackward(False, 2)     # 向左移动两个光标，如果是True的话，向左移动的同时，选中内容
#     # le.cursorForward(True, 3)
#     # le.cursorWordForward(True)    # 选中单词
#     le.home(False)   # 快速移动到行首
#     le.end(False)    # 快速移动到行尾
#     le.setCursorPosition(len(le.text())/2)          #自定义设置光标移动的地方
#     print(le.cursorPositionAt(QPoint(15, 5)))
#     le.setFocus()
# btn.pressed.connect(cursor_move)
#


# *****************设置文本外边距*****************
le.resize(200, 300)
le.setTextMargins(100, 0, 0, 0)  # 左上右下
# *****************对齐操作*****************
le.setAlignment(Qt.AlignRight | Qt.AlignBottom)    # 两种对齐方式





# *****************信号*****************
le2 = QLineEdit(window)
le.returnPressed.connect(lambda : le2.setFocus())
le.editingFinished.connect(lambda :print("结束编辑"))

le.cursorPositionChanged.connect(lambda old_pos, new_pos: print(old_pos, new_pos))   # lambda 函数还可以设置形参




















# 2.3 展示控件
QShortcut(QKeySequence(window.tr("Ctrl+W")), window, window.close)
window.show()
# 3. 应用程序的执行
sys.exit(app.exec())