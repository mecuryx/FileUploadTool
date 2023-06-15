import sys
import PyQt5.QtCore
from PyQt5.QtWidgets import *
from util.iniParse import INIRWTool
from page.addServer_ui import Ui_AddServerPage


class AddServer(Ui_AddServerPage,QWidget):

    # 定义信号
    addSignal = PyQt5.QtCore.pyqtSignal()
    logSignal = PyQt5.QtCore.pyqtSignal(str)

    def __init__(self):
        super(AddServer,self).__init__()
        self.setupUi(self)
        self.iNIRWTool = INIRWTool()
        self.btn_saveServer.clicked.connect(self.save)
        self.btn_closeServer.clicked.connect(self.closeDialog)

    def save(self):
        serverName = self.le_newServerName.text()
        ip = self.le_new_ip.text()
        port = self.le_new_port.text()
        user = self.le_new_user.text()
        passwd = self.le_new_passwd.text()
        if serverName == '':
            self.logSignal.emit("请输入环境名！")
        elif ip == '':
            self.logSignal.emit("请输入ip！")
        elif port == '':
            self.logSignal.emit("请输入port！")
        elif user == '':
            self.logSignal.emit("请输入用户！")
        elif passwd == '':
            self.logSignal.emit("请输入密码！")
        else:
            for section in self.iNIRWTool.getAllSections():
                if section == serverName:
                    self.logSignal.emit("重复不可添加！")
                    return
            self.iNIRWTool.addSection(serverName)
            self.iNIRWTool.addItems(serverName,'conn_ip', ip)
            self.iNIRWTool.addItems(serverName, 'conn_port', port)
            self.iNIRWTool.addItems(serverName, 'conn_user', user)
            self.iNIRWTool.addItems(serverName, 'conn_passwd', passwd)
            self.closeDialog()
            self.logSignal.emit('添加环境成功')
            self.addSignal.emit()     # 向父窗口发射信号
    def closeDialog(self):
        self.close()

    def closeEvent(self, event):
        self.le_newServerName.clear()
        ip = self.le_new_ip.clear()
        port = self.le_new_port.clear()
        user = self.le_new_user.clear()
        passwd = self.le_new_passwd.clear()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    addServer = AddServer()
    addServer.show()
    sys.exit(app.exec_())
