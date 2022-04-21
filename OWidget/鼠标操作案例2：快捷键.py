# 创建一个窗口，监听用户按键，
# 要求 1.监听用户输入Tab键，2.监听用户输入command+s 组合键  3.监听用户输入command+w

from PyQt5.Qt import *
import sys
class MyLabel(QLabel):
    def keyPressEvent(self, evt):
        print("点击了键盘")  # 用以测试这种方法是否被正常调用
        # # QKeyEvent   # command QKeyEvent去查看它拥有的方法
        # if evt.key() == Qt.Key_Tab:   # 用这条语句测试某个键是否属于key这种类型的键 （普通键） 修饰键是ctrl、comman、F1这种
        #     print("用户点击了tab")

        # 组合键
        if evt.modifiers() == Qt.ControlModifier and evt.key() == Qt.Key_W:
            print("command+W 退出窗口")
        if evt.modifiers() == Qt.MetaModifier and evt.key() == Qt.Key_W:
            print("ctrl+W 退出窗口")
        # 两个相同类型的键
        if evt.modifiers() == Qt.MetaModifier | Qt.ShiftModifier:
            print("两个修饰键一起运行")

        # 三个组合键
        if evt.modifiers() == Qt.MetaModifier | Qt.ShiftModifier and evt.key() == Qt.Key_R :   # 前面用或运算  把两个值或运算了，"加起来"代表三个键满足
            print("ctrl+Shfit+R 运行")
# 1. 创建一个对象
app = QApplication(sys.argv)

# 2. 控件的操作
# 2.1 创建控件
window = QWidget()
# 2.2 设置控件
window.setWindowTitle("")
window.resize(500, 500)

label = MyLabel(window)    # 创建label标签，是因为要标签控件
label.grabKeyboard()    # 捕获键盘的操作
# 2.3 展示控件
window.show()
# 3. 应用程序的执行
sys.exit(app.exec())