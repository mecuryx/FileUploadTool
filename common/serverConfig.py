import sys
from page.serverConfig_ui import Ui_ServerConfigPage
from PyQt5.QtWidgets import *
from util.iniParse import INIRWTool
import PyQt5.QtCore
from common.addParams import AddParams

class ServerConfig(QWidget,Ui_ServerConfigPage):

    # 定义信号
    logSignal = PyQt5.QtCore.pyqtSignal(str)
    serverName = ''
    def __init__(self):
        super(ServerConfig, self).__init__()
        self.setupUi(self)
        self.iNIRWTool = INIRWTool()
        self.addParams = AddParams()

        #self.serverName = serverName  # 由主窗口传来的所选择的环境
        #self.fillConnect(self.serverName)
        #self.fillInfo(self.serverName)    #加载配置详情

        self.btn_addParam.clicked.connect(self.addService)
        self.btn_delParam.clicked.connect(self.delService)
        self.btn_updateParam.clicked.connect(self.updateService)
        self.addParams.addSignal.connect(self.fillInfo)


       # self.tw_serverConfig.itemChanged.connect(self.updateParam)

    def setServerName(self, serverName):
        self.serverName = serverName  # 由主窗口传来的所选择的环境

    # 根据选择环境填充连接信息和服务信息
    def fillInfo(self, text):

        try:
            options = self.iNIRWTool.getItems(text)
            options_serv = list(filter(lambda option: 'serv' in option, options))
            self.setModle(self.tw_serverConfig, options_serv, text)

        except Exception as e:
            self.logSignal.emit("加载失败！")
    def fillConnect(self, text):
        try:
            self.le_config_ip.setText(self.iNIRWTool.get(text, "conn_ip"))
            self.le_config_port.setText(self.iNIRWTool.get(text, "conn_port"))
            self.le_config_user.setText(self.iNIRWTool.get(text, "conn_user"))
            self.le_config_passwd.setText(self.iNIRWTool.get(text, "conn_passwd"))
        except Exception as e:
            self.logSignal.emit("加载失败，请检查文件配置！")

    # 设置表格样式,加载数据
    def setModle(self, tableWidget, options, text):
        tableWidget.setRowCount(len(options))
        tableWidget.setColumnCount(2)
        # 设置服务配置列表表头
        tableWidget.setHorizontalHeaderLabels(['参数名', '参数值'])
        tableWidget.setSelectionBehavior(QAbstractItemView.SelectRows)
        # 垂直拉伸填充表格
        header = tableWidget.horizontalHeader()
        header.setSectionResizeMode(QHeaderView.Stretch)
        for i in range(len(options)):
            newItem = QTableWidgetItem(str(options[i][5:]))  # 插入参数名
            tableWidget.setItem(i, 0, newItem)
            newItem = QTableWidgetItem(str(self.iNIRWTool.get(text, options[i])))  # 插入参数值
            tableWidget.setItem(i, 1, newItem)

    def addService(self):

        #serviceName = self.tw_serverConfig.currentItem().text()

        self.addParams.setServiceName(self.serverName)
        self.addParams.type = 'add'
        self.addParams.show()


    def delService(self):
        row = self.tw_serverConfig.selectedItems()
        print(len(row))
        if len(row) == 0:
            self.logSignal.emit("请选择后在进行删除！")
        else:
            print(self.serverName, 'serv_' + row[0].text())
            self.iNIRWTool.delete(self.serverName, 'serv_' + row[0].text())

            self.fillInfo(self.serverName)
            self.logSignal.emit("删除服务成功！")


    def updateService(self):

        rowCount = self.tw_serverConfig.currentRow()
        if rowCount < 0:
            self.logSignal.emit("请选择后再进行修改！")
            QMessageBox.about(self, '提示', '请选择后再进行修改！')
        else:
            self.addParams.setServiceName(self.serverName)
            self.addParams.type = 'update'
            key = self.tw_serverConfig.item(rowCount,0).text()
            value = self.tw_serverConfig.item(rowCount,1).text()
            self.addParams.setParam(key,value)
            self.addParams.show()
            #print(value,self.tw_serverConfig.cursor())

    def closeEvent(self, event):

        self.le_config_ip.setText('')
        self.le_config_port.setText('')
        self.le_config_user.setText('')
        self.le_config_passwd.setText('')


if __name__ == '__main__':
    app = QApplication(sys.argv)
    service = ServerConfig()
    service.show()
    sys.exit(app.exec_())