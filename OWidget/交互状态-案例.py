# 要求，默认状态：标签隐藏、文本框和按钮显示、按钮设置为不可用状态
# 当文本框有内容时，按钮可用，否则不可用
# 当文本框内容为Hello时，点击按钮则显示标签，并展示文本为登陆成功，否则为失效
from PyQt5.Qt import *

class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("交互状态案例")
        self.resize(500, 500)
        self.setup_ui()

    def setup_ui(self):
        # 添加三个子控件：文本框、按钮、标签
        label = QLabel(self)   # 这个label属于一个窗口，窗口是self
        label.setText("我是标签")
        label.move(100, 50)
        label.hide()     # 把标签隐藏

        txt = QLineEdit(self)
        # text.setText("我是文本框")
        txt.move(100, 100)

        btn = QPushButton(self)
        btn.setText("我是按钮")
        btn.move(100, 150)
        btn.setEnabled(False)    # 设置按钮不可用
        def text_cao(text_content):
            print("文本内容发生改变", text_content)
            # if len(text) > 0:
            #     btn.setEnabled(True)
            # else:
            #     btn.setEnabled(False)

            # 对上面判断语句的一个优化
            btn.setEnabled(len(text_content)>0)

        txt.textChanged.connect(text_cao)
        def press_cao():
            print("标签被点击")
            # 获取文本框内容，是的话显示隐藏的标签，展示文本：登陆成功
            content = txt.text()
            if content == "Hello":
                label.setVisible(True)
                label.setText("登陆成功")
            else:
                label.setText("登陆失败")
            label.adjustSize()   # 根据自身内容，调节尺寸大小，避免label的text太长而无法展示

        btn.pressed.connect(press_cao)



#  测试这些类里的功能是否有效，该py下面的类被其他文件调用的时候，不会运行这个main。仅用于功能测试

if __name__ == '__main__':
    import sys
    app = QApplication(sys.argv)

    window =Window()
    window.show()
    sys.exit(app.exec())