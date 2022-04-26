# *****************抽象按钮组*****************
# QButtionGroup 属于 QObject，不可见
from PyQt5.Qt import *
import sys
# 1. 创建一个对象
app = QApplication(sys.argv)

# 2. 控件的操作
# 2.1 创建控件
window = QWidget()
# 2.2 设置控件
window.setWindowTitle("按钮组的使用")
window.resize(500, 500)

# 创建四个单选按钮
rb_nan = QRadioButton("male", window)
rb_nan.move(100, 100)
rb_nv = QRadioButton("Female", window)
rb_nv.move(100, 150)

# 设置性别分组
sex_group = QButtonGroup(window)
sex_group.addButton(rb_nv, 1)    # 设置ID，方便后续使用
sex_group.addButton(rb_nan, 2)

rb_yes = QRadioButton("yes", window)
rb_yes.move(200, 100)
rb_no = QRadioButton("no", window)
rb_no.move(200, 150)

# 设置是否分组
whether_group = QButtonGroup(window)
whether_group.addButton(rb_yes)
whether_group.addButton(rb_no)

# 获取组里某ID的信息
print(sex_group.button(1))
# 获取当前选择按钮(先设置一个默认的）
rb_nv.setChecked(True)
print(sex_group.checkedButton())



# 2.3 展示控件
window.show()
# 3. 应用程序的执行
sys.exit(app.exec())