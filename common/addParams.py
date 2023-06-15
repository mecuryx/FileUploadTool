from PyQt5.QtWidgets import *
from page.addParams_ui import Ui_AddParamsPage
from util.iniParse import INIRWTool
import PyQt5.QtCore


class AddParams(Ui_AddParamsPage,QWidget):

    serverName = None
    type = None
    # 定义信号
    addSignal = PyQt5.QtCore.pyqtSignal(str)
    logSignal = PyQt5.QtCore.pyqtSignal(str)

    def __init__(self):
        super(AddParams, self).__init__()

        self.setupUi(self)
        self.iNIRWTool = INIRWTool()

        # 定义槽函数
        self.btn_saveParam.clicked.connect(self.addParam)
        self.btn_cancelParam.clicked.connect(self.closeDialog)

    def setParam(self, paramkey,paramValue):
        self.le_config_key.setText(paramkey)
        self.le_config_key.setEnabled(False)
        self.le_config_value.setText(paramValue)

    def setServiceName(self, serverName):
        self.serverName = serverName  # 由主窗口传来的所选择的服务

    def addParam(self, type):
        type = self.type
        flag = True
        key = self.le_config_key.text()
        value = self.le_config_value.text()
        if key == "" or value == "":
            QMessageBox.about(self, '提示', '请填写参数名和参数值！')
        else:
            if type == 'add':
                key = 'serv_' + key
                serviceNames = self.iNIRWTool.getAllServiceName(self.serverName)
                for serviceName in serviceNames:
                    if serviceName == str('serv_'+key):
                        QMessageBox.about(self, '提示', '服务名已存在！')
                        flag = False
            if flag:
                key = 'serv_' + key
                self.iNIRWTool.addItems(self.serverName, key, value)
                self.addSignal.emit(self.serverName)
                if type == 'update':
                    QMessageBox.about(self, '提示', '修改服务成功！')
                else:
                    QMessageBox.about(self, '提示', '添加服务成功！')
                self.closeDialog()
                self.le_config_key.clear()
                self.le_config_value.clear()

    def updateParam(self):
        key = self.le_config_key.text()
        value = self.le_config_value.text()
        if value == "":
            QMessageBox.about(self, '提示', '请填写参数值！')
        else:
            key = 'serv_' + key
            self.iNIRWTool.addItems(self.serverName, key, value)
            self.addSignal.emit(self.serverName)
            QMessageBox.about(self, '提示', '修改服务成功！')
            self.closeDialog()
            self.le_config_key.clear()
            self.le_config_value.clear()
            self.le_config_key.setEnabled(True)

    def closeDialog(self):
        self.close()

    def closeEvent(self, event):
        self.le_config_key.setEnabled(True)
        self.le_config_key.clear()
        self.le_config_value.clear()