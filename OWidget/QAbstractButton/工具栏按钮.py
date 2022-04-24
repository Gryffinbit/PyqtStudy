from PyQt5.Qt import *
import sys
# 1. 创建一个对象
app = QApplication(sys.argv)

# 2. 控件的操作
# 2.1 创建控件
window = QWidget()
# 2.2 设置控件
window.setWindowTitle("QToolButton")
window.resize(500, 500)

tb = QToolButton(window)
# tb.setText("hello")
# tb.setIcon(QIcon("../../心心相印.png"))
# tb.setIconSize(QSize(50, 50))
#
# # 鼠标放在图标上，会显示tip
# tb.setToolTip("这是爱你的开关")
# # 设置按钮风格
# tb.setToolButtonStyle(Qt.ToolButtonTextOnly)    # 只有文字
# # tb.setToolButtonStyle(Qt.ToolButtonIconOnly)    # 只有图标
# # tb.setToolButtonStyle(Qt.ToolButtonTextUnderIcon)   #文本显示在图标下方
# # tb.setToolButtonStyle(Qt.ToolButtonTextBesideIcon)   # 文本显示在图标旁边
#


# *****************设置箭头图标*****************
# Qt.NoArrow   无箭头
# Qt.UpArrow   向上箭头
tb.setArrowType(Qt.LeftArrow)













# 2.3 展示控件
window.show()
# 3. 应用程序的执行
sys.exit(app.exec())