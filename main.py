import sys
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import (QWidget, QToolTip, QPushButton, QApplication, QDesktopWidget, QLabel, QHBoxLayout,
                             QVBoxLayout, QLineEdit, QGridLayout, QMainWindow, QComboBox)
from PyQt5.Qt import *
from PyQt5.QtGui import QIcon, QPixmap

# 导入机器学习文件
import test

global record
record= [["",""]]
all_set = [[], ["192.168.1.104", "IPad"], ["192.168.1.101", "IPhone"], ["192.168.1.108", "华为手机"],
           ["192.168.1.110", "路由器"], ["192.168.1.103", "电视"]]


class Example(QWidget):

    def __init__(self):
        super().__init__()
        # 用来记录所有识别过的IP及设备身份
        self.initUI()

    def initUI(self):
        self.resize(1200, 800)
        self.center()
        self.setWindowTitle('物联网设备识别系统')
        self.setWindowIcon(QIcon('logo.JPG'))

        # 设置检测系统图片
        palette = QPalette()
        pix = QPixmap("system.jpg")
        pix = pix.scaled(self.width(), self.height())
        palette.setBrush(QPalette.Background, QBrush(pix))
        self.setPalette(palette)

        # 设置文件输入框
        self.member1 = QLabel(self)
        self.member1.setText('''请选择需要检测的文件''')
        self.member1.setAlignment(Qt.AlignCenter)
        self.member1.setStyleSheet("font-size:30px;""font-family:微软雅黑;")
        self.member1.setFixedSize(300, 50)
        self.member1.move(80, self.height() / 2 - 50)

        # self.member1.set
        # self.member2.set

        # 设置文件选择框
        self.combo_choose_file = QComboBox(self)
        self.combo_choose_file.addItem("unknown1.csv")
        self.combo_choose_file.addItem("unknown2.csv")
        self.combo_choose_file.addItem("unknown3.csv")
        self.combo_choose_file.addItem("unknown4.csv")
        self.combo_choose_file.addItem("unknown5.csv")
        self.combo_choose_file.setStyleSheet("font-size:25px;""font-family:微软雅黑;")
        self.combo_choose_file.resize(200, 50)
        self.combo_choose_file.move(430, self.height() / 2 - 50)

        # 设置"开始检测"控件
        self.btn_start = QPushButton(self)
        self.btn_start.setFixedSize(150, 50)
        self.btn_start.setText("开始检测")
        self.btn_start.setStyleSheet('''background-color:rgb(0,153,
        255);font-size:30px;font-family:微软雅黑;border-radius:5px;''')
        self.btn_start.move(680, self.height() / 2 - 50)
        # 点击按钮时候 的 事件响应函数
        self.btn_start.clicked.connect(self.train_and_return_result)

        # 设置"展示所有识别过的设备"控件
        self.btn_start = QPushButton(self)
        self.btn_start.setFixedSize(200, 50)
        self.btn_start.setText("设备识别记录")
        self.btn_start.setStyleSheet(
            '''background-color:rgb(211,211,211);font-size:30px;font-family:微软雅黑;border-radius:5px;''')
        self.btn_start.move(880, self.height() / 2 - 50)
        # 点击按钮时候 的 事件响应函数
        self.btn_start.clicked.connect(self.show_all_device)

        self.show()

        self.member2 = show_record()

    def train_and_return_result(self):
        global record
        result = test.identify(self.combo_choose_file.currentText())
        #QMessageBox.information(self,"识别结果","1")
        if result == 0:
            QMessageBox.information(self,"识别结果", "识别失败")
        elif result == 1:
            QMessageBox.information(self, "识别结果", str(all_set[result]))
        elif result == 2:
            QMessageBox.information(self, "识别结果", str(all_set[result]))
        elif result == 3:
            QMessageBox.information(self, "识别结果", str(all_set[result]))
        elif result == 4:
            QMessageBox.information(self, "识别结果", str(all_set[result]))
        elif result == 5:
            QMessageBox.information(self, "识别结果", str(all_set[result]))


        record.append(all_set[result])



    # 控制窗口显示在屏幕中心
    def center(self):
        # 获得窗口
        qr = self.frameGeometry()
        # 获得屏幕中心点
        cp = QDesktopWidget().availableGeometry().center()
        # 显示到屏幕中心
        qr.moveCenter(cp)
        self.move(qr.topLeft())

    # 显示所有已经识别的设备信息
    def show_all_device(self):
        self.member2.shownew()


class show_record(QWidget):
    def __init__(self):

        super().__init__()  # 使用super函数可以实现子类使用父类的方法
        self.setWindowTitle("设备识别记录")
        self.setWindowIcon(QIcon('logo.JPG'))  # 设置窗口图标
        self.resize(600, 600)
        self.text_browser = QTextBrowser(self)  # 实例化一个QTextBrowser对象
        self.text_browser.setText("<h1>所有识别过的记录如下：</h1>")  # 设置编辑框初始化时显示的文本
        self.close_button = QPushButton("Close", self)
        self.clear_button = QPushButton("Clear", self)

        self.close_button.clicked.connect(self.close_event)
        self.clear_button.clicked.connect(self.clear_record)

        self.h_layout = QHBoxLayout()
        self.v_layout = QVBoxLayout()

        self.h_layout.addWidget(self.clear_button)
        self.h_layout.addWidget(self.close_button)
        self.v_layout.addWidget(self.text_browser)
        self.v_layout.addLayout(self.h_layout)
        self.setLayout(self.v_layout)


    def clear_record(self):
        global record
        record.clear()
        self.close()
        self.__init__()
        self.show()

    def shownew(self):
        count = 1
        print(record)
        while(count<len(record)):
            self.text_browser.append("<h2>%d、IP为%s的设备为：%s</h2>" % (count, record[count][0], record[count][1]))
            count += 1

        self.show()

    def close_event(self):
        self.close()


if __name__ == '__main__':
    # 创建应用程序和对象
    app = QApplication(sys.argv)
    mainWindow = Example()
    sys.exit(app.exec_())
