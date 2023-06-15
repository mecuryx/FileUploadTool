import os
import sys
import datetime

from PyQt5.QtWidgets import *
import paramiko
import re
from addServer import AddServer
from serverConfig import ServerConfig
from addParams import AddParams
from util.logging import Log
from util.iniParse import INIRWTool
from page.file_upload_ui import Ui_MainWindow


class MainPage(QMainWindow,Ui_MainWindow):
    def __init__(self):
        super(MainPage,self).__init__()
        self.setupUi(self)

        self.transport=None   #传输对象
        self.sftp = False
        self.ssh = None   #通道
        self.localFile = ''   #本地文件路径
        self.delServerDialog = None
        self.iNIRWTool = INIRWTool()
        self.serverAdd = AddServer()   #定义为全局变量，否则会闪退
        self.configServer = ServerConfig()
        self.addParams = AddParams()
        self.log = Log(self.tb_log)


        '''
        # 下拉款加载配置
        #  实例化configParser对象
        self.page = configparser.ConfigParser()

        try:
            # -read读取ini文件
            self.page.read('servicesConfig.ini', encoding='UTF-8')
        except Exception as e:
            self.printLog("打开文件错误！")
        '''
        sections = self.iNIRWTool.getAllSections()
        self.cb_selectEnvir.addItem('请选择')
        for section in sections:
            self.cb_selectEnvir.addItem(section)
        self.setButtonState(False)

        # 绑定槽函数
        self.cb_selectEnvir.activated[str].connect(self.fillInfo)   # 条目发生改变，发射信号，传递条目内容
        self.btn_reset.clicked.connect(self.reset)
        self.btn_clear.clicked.connect(self.clearLog)
        self.btn_connect.clicked.connect(self.connectServer)
        self.btn_disConnect.clicked.connect(self.closeServer)
        self.btn_upload.clicked.connect(self.upload)
        self.btn_selectFile.clicked.connect(self.selectFile)
        self.btn_uploadAndApply.clicked.connect(self.uploadAndApply)
        self.btn_findServer.clicked.connect(self.findServers)
        self.btn_addServer.clicked.connect(self.addServer)
        self.btn_delServer.clicked.connect(self.defServerOrNot)
        self.btn_serverConfig.clicked.connect(self.serverConfig)


        # 添加窗口信号槽
        self.serverAdd.addSignal.connect(self.findServers)
        self.serverAdd.logSignal.connect(self.log.printLog)
        self.configServer.logSignal.connect(self.log.printLog)
        self.addParams.logSignal.connect(self.log.printLog)

    def setButtonState(self,state):
        self.btn_disConnect.setEnabled(state)
        self.btn_uploadAndApply.setEnabled(state)
        self.btn_upload.setEnabled(state)
        self.btn_selectFile.setEnabled(state)
    # 连接服务器
    def connectServer(self):
        
        self.host = self.le_ip.text()
        self.port = self.le_port.text()
        self.passwd = self.le_passwd.text()
        self.user = self.le_user.text()

        try:

            if self.transport is None or not self.transport.is_active():
                # 使用Transport上传
                self.transport = paramiko.Transport((self.host,int(self.port)))
                self.transport.banner_timeout = 60
                self.transport.connect(username=self.user,password=self.passwd)
                self.sftp = paramiko.SFTPClient.from_transport(self.transport)
                # 使用SSHClient执行命令
                self.ssh = paramiko.SSHClient()
                self.ssh._transport = self.transport
                self.setButtonState(True)
            self.log.printLog("已连接！！")
        except:
            self.log.printLog('连接失败！')  # 打印日志信息

    def send_command(self,cmd):
       # print(cmd)
        stdin, stdout, stderr = self.ssh.exec_command(cmd)

        return stdout.read().decode('utf-8')

    # 关闭服务器连接
    def closeServer(self):
        if self.transport is not None:
            self.transport.close()
            self.setButtonState(False)
        if self.ssh is not None:
            self.ssh.close()
        self.log.printLog("已断开！！")


    # 根据选择环境填充连接信息和服务信息
    def fillInfo(self,text):
        if '请选择' == text:
            self.tw_services.setRowCount(0)
            self.reset()
            return
        try:
            self.le_ip.setText(self.iNIRWTool.get(text,"conn_ip"))
            self.le_port.setText(self.iNIRWTool.get(text, "conn_port"))
            self.le_user.setText(self.iNIRWTool.get(text, "conn_user"))
            self.le_passwd.setText(self.iNIRWTool.get(text, "conn_passwd"))

            options = self.iNIRWTool.getItems(text)
            options_serv=list(filter(lambda option:'serv' in option,options))

            self.setModle(self.tw_services, options_serv, text)

        except:
            self.log.printLog("加载失败，请检查文件配置！")


    # 清空输入框
    def reset(self):
        self.le_ip.clear()
        self.le_port.clear()
        self.le_user.clear()
        self.le_passwd.clear()
        #self.printLog("清空输入框！")

    # 清空日志
    def clearLog(self):
        self.log.clearLog()
    # 打开文件
    def selectFile(self):
        open_filename = QFileDialog.getOpenFileName(None, '选择文件', '', 'All files(*.*)')
        if open_filename[0] != '':
            self.localFile = open_filename[0]
            self.log.printLog("已选中文件："+self.localFile)
    # 上传文件
    def upload(self):
        try:
            localFile = self.localFile
            if self.cbox_customUpload.isChecked():
                targetFile = self.le_serverPath.text() + '/' + os.path.basename(localFile)
            else:
                items = self.tw_services.selectedItems()
                targetFile = items[1].text() + '/' + os.path.basename(localFile)
            self.sftp.put(localFile, targetFile)  # 上传
            self.log.printLog("文件已上传！")
        except:
            self.log.printLog("上传失败，请检查是否已连接或上传路径正确！")

    # 上传并部署
    def uploadAndApply(self):
        try:
            path = self.tw_services.selectedItems()[1].text()
            fileName = os.path.basename(self.localFile)
            now = datetime.datetime.now().strftime('%Y%m%d%H%M%S')
            if fileName.split('.')[1] == 'zip':
                self.upload()
                cmd = 'cd '+path+';mv dist dist'+now+';unzip '+fileName
                self.send_command(cmd)
                self.log.printLog('前端文件已替换！')
            elif fileName.split('.')[1] == 'jar':
                self.send_command('cd ' + path + ';mv ' + fileName + ' ' + fileName + now)  # 备份
                self.upload()
                # 部署并重启
                lines = self.send_command('ps -ef|grep '+fileName).split('\n')
                if len(lines) > 0:
                    for line in lines:
                        temp = 'java.+jar'
                        if re.search(temp, line) is not None:
                            # 获取进程号
                            processNo = re.findall('\d+', line)[0]
                            # 根据进程号获取路径
                            res = self.send_command('pwdx %s' % processNo)
                            pathStr = res.split(':')[1].strip()
                            if pathStr == path:
                                self.send_command('kill -9 %s' % processNo)
                                self.ssh.exec_command('cd '+path+';source /etc/profile;sh start.sh')

                                self.log.printLog('已重新部署！')
                                break
            else:
                self.log.printLog("不支持的文件类型,请重新选择!")
        except:
            self.log.printLog("上传部署失败！")

    # 设置表格样式,加载数据
    def setModle(self,tableWidget,options,text):
        tableWidget.setRowCount(len(options))
        tableWidget.setColumnCount(2)
        # 设置服务配置列表表头
        tableWidget.setHorizontalHeaderLabels(['参数名', '参数值'])
        tableWidget.setSelectionBehavior(QAbstractItemView.SelectRows)
        # 垂直拉伸填充表格
        header = tableWidget.horizontalHeader()
        header.setSectionResizeMode(QHeaderView.Stretch)
        for i in range(len(options)):
            newItem = QTableWidgetItem(str(options[i][5:]))#插入参数名
            tableWidget.setItem(i, 0, newItem)
            newItem = QTableWidgetItem(str(self.iNIRWTool.get(text,options[i])))#插入参数值
            tableWidget.setItem(i, 1, newItem)
    # 通过选择的项目来加载配置
    def listService(self,text):
        if '请选择' == text:
            self.tw_configItems.setRowCount(0)
            return
        options = self.iNIRWTool.getItems(text)
        self.setModle(self.tw_configItems,options,text)


    '''
        ####基本配置######    
    '''
    # 查询环境
    def findServers(self):
        self.lw_serverList.clear()
        if self.le_serverName.text() == '':
            sections = self.iNIRWTool.getAllSections()
        else:
            sections = self.iNIRWTool.getSectionByInput(self.le_serverName.text())
        print(sections)
        self.lw_serverList.setObjectName("lw_serverList")
        self.lw_serverList.setAlternatingRowColors(True)
        for section in sections:
            self.lw_serverList.addItem(section)
    '''
        self.lw_serverList.setStyleSheet("QListWidget#lw_serverList{background-color:rgb(255,255,255);border:0px;}"
                                     "QListWidget#lw_serverList::item{color:white;height:40px;background-color:rgb("
                                     "100,64,82);border:0px;} "
                                     "QListWidget#lw_serverList:nth-of-type(odd){color:red}"
                                     )
    '''
    # 增加环境
    def addServer(self):
        self.serverAdd.show()

    def delServer(self):
        if self.lw_serverList.currentItem() == None:
            self.log.printLog("请选择环境！")
        else:
            serverName = self.lw_serverList.currentItem().text()
            self.iNIRWTool.delSectionByName(serverName)
            self.log.printLog("删除环境成功！")
            self.findServers()

    def defServerOrNot(self):
        reply = QMessageBox.information(self, "注意", "同时删除环境和所有服务配置，是否继续？",
                                QMessageBox.Ok | QMessageBox.Cancel, QMessageBox.Ok)
        if reply == QMessageBox.Ok:
            self.delServer()

    def serverConfig(self):
        if self.lw_serverList.currentItem() == None:
            self.log.printLog("请选择环境！")
        else:
            serverName = self.lw_serverList.currentItem().text()
            self.configServer.setServerName(serverName)
            self.configServer.fillConnect(serverName)
            self.configServer.fillInfo(serverName)
            #self.configServer = ServerConfig(serverName)
            self.configServer.show()
if __name__ == '__main__':
    app = QApplication(sys.argv)
    mPage = MainPage()
    mPage.show()
    sys.exit(app.exec_())
