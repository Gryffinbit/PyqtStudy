from PyQt5.Qt import *
import sys
# 1. 创建一个对象
app = QApplication(sys.argv)

# 2. 控件的操作
# 2.1 创建控件
window = QWidget()
# 2.2 设置控件
window.setWindowTitle("命令链接按钮的使用")
window.resize(500, 500)

btn = QCommandLinkButton("标题", "描述", window)
btn.setText("标题2")
btn.setDescription("helloworld")
btn.setIcon(QIcon("../../心心相印.png"))
# 2.3 展示控件
window.show()
# 3. 应用程序的执行
sys.exit(app.exec())