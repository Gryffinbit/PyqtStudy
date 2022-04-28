# 封装的类--功能部分
from PyQt5.Qt import *
# class AgeVadidator(QValidator):
#     def validate(self, input_str, pos_int):     # 输入字符串和光标的位置
#         print(input_str, pos_int)
#         if 18 <= int(input_str) <= 180:
#             return (QValidator.Acceptable, input_str, pos_int)
#         elif 1 <= int(input_str) <= 17:
#             return (QValidator.Intermediate, input_str, pos_int)
#         else:
#             return (QValidator.Invalid, input_str, pos_int)

class Window(QWidget):
    def __init__(self):
        super().__init__()
        QShortcut(QKeySequence(self.tr("Ctrl+W")), self, self.close)
        self.setWindowTitle("验证器的使用")
        self.resize(500, 500)
        self.setup_ui()

    def setup_ui(self):
        le = QLineEdit(self)
        le.move(100, 100)
        # 年龄限制 18～180
        # 创建一个验证器对象,并且要实例化，即自己写class，继承自QValidator

        btn = QPushButton(self)
        btn.move(100, 300)
        btn.setText("button")
# *****************设置掩码*****************
# 总共输入5位，左边2（必须是大写字母） 右边2（必须是一个数字）
        le.setInputMask(">AA-9A")
# *****************是否被编辑*****************
        btn.pressed.connect(lambda : print(le.isModified()))















#  测试这些类里的功能是否有效，该py下面的类被其他文件调用的时候，不会运行这个main。仅用于功能测试

if __name__ == '__main__':
    import sys
    app = QApplication(sys.argv)
    window = Window()
    window.show()
    sys.exit(app.exec())