# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'file_upload_ui.ui'
#
# Created by: PyQt5 UI code generator 5.15.7
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(787, 615)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.tabw_fileUpload = QtWidgets.QTabWidget(self.centralwidget)
        self.tabw_fileUpload.setGeometry(QtCore.QRect(0, 0, 791, 451))
        self.tabw_fileUpload.setObjectName("tabw_fileUpload")
        self.tab_upload = QtWidgets.QWidget()
        self.tab_upload.setObjectName("tab_upload")
        self.btn_reset = QtWidgets.QPushButton(self.tab_upload)
        self.btn_reset.setGeometry(QtCore.QRect(580, 130, 81, 31))
        self.btn_reset.setObjectName("btn_reset")
        self.labe_ip = QtWidgets.QLabel(self.tab_upload)
        self.labe_ip.setGeometry(QtCore.QRect(80, 40, 71, 16))
        self.labe_ip.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.labe_ip.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.labe_ip.setFrameShadow(QtWidgets.QFrame.Plain)
        self.labe_ip.setObjectName("labe_ip")
        self.btn_upload = QtWidgets.QPushButton(self.tab_upload)
        self.btn_upload.setGeometry(QtCore.QRect(450, 330, 81, 31))
        self.btn_upload.setObjectName("btn_upload")
        self.le_ip = QtWidgets.QLineEdit(self.tab_upload)
        self.le_ip.setGeometry(QtCore.QRect(160, 30, 161, 31))
        self.le_ip.setObjectName("le_ip")
        self.le_port = QtWidgets.QLineEdit(self.tab_upload)
        self.le_port.setGeometry(QtCore.QRect(410, 30, 161, 31))
        self.le_port.setObjectName("le_port")
        self.labe_port = QtWidgets.QLabel(self.tab_upload)
        self.labe_port.setGeometry(QtCore.QRect(370, 40, 41, 16))
        self.labe_port.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.labe_port.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.labe_port.setFrameShadow(QtWidgets.QFrame.Plain)
        self.labe_port.setObjectName("labe_port")
        self.labe_user = QtWidgets.QLabel(self.tab_upload)
        self.labe_user.setGeometry(QtCore.QRect(80, 90, 71, 16))
        self.labe_user.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.labe_user.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.labe_user.setFrameShadow(QtWidgets.QFrame.Plain)
        self.labe_user.setObjectName("labe_user")
        self.labe_passwd = QtWidgets.QLabel(self.tab_upload)
        self.labe_passwd.setGeometry(QtCore.QRect(370, 90, 41, 16))
        self.labe_passwd.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.labe_passwd.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.labe_passwd.setFrameShadow(QtWidgets.QFrame.Plain)
        self.labe_passwd.setObjectName("labe_passwd")
        self.le_user = QtWidgets.QLineEdit(self.tab_upload)
        self.le_user.setGeometry(QtCore.QRect(160, 80, 161, 31))
        self.le_user.setObjectName("le_user")
        self.le_passwd = QtWidgets.QLineEdit(self.tab_upload)
        self.le_passwd.setGeometry(QtCore.QRect(410, 80, 161, 31))
        self.le_passwd.setObjectName("le_passwd")
        self.btn_connect = QtWidgets.QPushButton(self.tab_upload)
        self.btn_connect.setGeometry(QtCore.QRect(450, 200, 81, 31))
        self.btn_connect.setObjectName("btn_connect")
        self.btn_disConnect = QtWidgets.QPushButton(self.tab_upload)
        self.btn_disConnect.setGeometry(QtCore.QRect(580, 200, 81, 31))
        self.btn_disConnect.setObjectName("btn_disConnect")
        self.btn_uploadAndApply = QtWidgets.QPushButton(self.tab_upload)
        self.btn_uploadAndApply.setGeometry(QtCore.QRect(590, 330, 81, 31))
        self.btn_uploadAndApply.setObjectName("btn_uploadAndApply")
        self.cb_selectEnvir = QtWidgets.QComboBox(self.tab_upload)
        self.cb_selectEnvir.setGeometry(QtCore.QRect(640, 0, 141, 31))
        self.cb_selectEnvir.setObjectName("cb_selectEnvir")
        self.tw_services = QtWidgets.QTableWidget(self.tab_upload)
        self.tw_services.setGeometry(QtCore.QRect(70, 170, 301, 241))
        self.tw_services.setObjectName("tw_services")
        self.tw_services.setColumnCount(0)
        self.tw_services.setRowCount(0)
        self.btn_selectFile = QtWidgets.QPushButton(self.tab_upload)
        self.btn_selectFile.setGeometry(QtCore.QRect(450, 260, 211, 31))
        self.btn_selectFile.setObjectName("btn_selectFile")
        self.labe_ip_2 = QtWidgets.QLabel(self.tab_upload)
        self.labe_ip_2.setGeometry(QtCore.QRect(80, 140, 71, 16))
        self.labe_ip_2.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.labe_ip_2.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.labe_ip_2.setFrameShadow(QtWidgets.QFrame.Plain)
        self.labe_ip_2.setObjectName("labe_ip_2")
        self.le_serverPath = QtWidgets.QLineEdit(self.tab_upload)
        self.le_serverPath.setGeometry(QtCore.QRect(160, 130, 161, 31))
        self.le_serverPath.setObjectName("le_serverPath")
        self.cbox_customUpload = QtWidgets.QCheckBox(self.tab_upload)
        self.cbox_customUpload.setGeometry(QtCore.QRect(410, 130, 91, 31))
        self.cbox_customUpload.setObjectName("cbox_customUpload")
        self.tabw_fileUpload.addTab(self.tab_upload, "")
        self.tab_config = QtWidgets.QWidget()
        self.tab_config.setObjectName("tab_config")
        self.btn_delServer = QtWidgets.QPushButton(self.tab_config)
        self.btn_delServer.setGeometry(QtCore.QRect(610, 100, 81, 31))
        self.btn_delServer.setObjectName("btn_delServer")
        self.lb_base_config = QtWidgets.QLabel(self.tab_config)
        self.lb_base_config.setEnabled(True)
        self.lb_base_config.setGeometry(QtCore.QRect(0, 0, 791, 21))
        self.lb_base_config.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.lb_base_config.setStyleSheet("")
        self.lb_base_config.setAlignment(QtCore.Qt.AlignCenter)
        self.lb_base_config.setObjectName("lb_base_config")
        self.le_serverName = QtWidgets.QLineEdit(self.tab_config)
        self.le_serverName.setGeometry(QtCore.QRect(130, 40, 161, 31))
        self.le_serverName.setObjectName("le_serverName")
        self.btn_serverConfig = QtWidgets.QPushButton(self.tab_config)
        self.btn_serverConfig.setGeometry(QtCore.QRect(500, 100, 81, 31))
        self.btn_serverConfig.setObjectName("btn_serverConfig")
        self.tw_configItems = QtWidgets.QTableWidget(self.tab_config)
        self.tw_configItems.setGeometry(QtCore.QRect(10, 450, 71, 71))
        self.tw_configItems.setObjectName("tw_configItems")
        self.tw_configItems.setColumnCount(0)
        self.tw_configItems.setRowCount(0)
        self.btn_findServer = QtWidgets.QPushButton(self.tab_config)
        self.btn_findServer.setGeometry(QtCore.QRect(500, 60, 81, 31))
        self.btn_findServer.setObjectName("btn_findServer")
        self.labe_ip_3 = QtWidgets.QLabel(self.tab_config)
        self.labe_ip_3.setGeometry(QtCore.QRect(70, 50, 51, 16))
        self.labe_ip_3.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.labe_ip_3.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.labe_ip_3.setFrameShadow(QtWidgets.QFrame.Plain)
        self.labe_ip_3.setObjectName("labe_ip_3")
        self.btn_addServer = QtWidgets.QPushButton(self.tab_config)
        self.btn_addServer.setGeometry(QtCore.QRect(610, 60, 81, 31))
        self.btn_addServer.setObjectName("btn_addServer")
        self.lw_serverList = QtWidgets.QListWidget(self.tab_config)
        self.lw_serverList.setGeometry(QtCore.QRect(190, 150, 351, 261))
        self.lw_serverList.setObjectName("lw_serverList")
        self.tabw_fileUpload.addTab(self.tab_config, "")
        self.tb_log = QtWidgets.QTextBrowser(self.centralwidget)
        self.tb_log.setGeometry(QtCore.QRect(10, 450, 771, 121))
        self.tb_log.setObjectName("tb_log")
        self.btn_clear = QtWidgets.QPushButton(self.centralwidget)
        self.btn_clear.setGeometry(QtCore.QRect(700, 450, 81, 31))
        self.btn_clear.setObjectName("btn_clear")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 787, 23))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.tabw_fileUpload.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "文件上传部署工具"))
        self.btn_reset.setText(_translate("MainWindow", "重置"))
        self.labe_ip.setText(_translate("MainWindow", "目标服务器"))
        self.btn_upload.setText(_translate("MainWindow", "上传"))
        self.labe_port.setText(_translate("MainWindow", "端口"))
        self.labe_user.setText(_translate("MainWindow", "用户名"))
        self.labe_passwd.setText(_translate("MainWindow", "密码"))
        self.btn_connect.setText(_translate("MainWindow", "连接"))
        self.btn_disConnect.setText(_translate("MainWindow", "断开连接"))
        self.btn_uploadAndApply.setText(_translate("MainWindow", "上传并部署"))
        self.btn_selectFile.setText(_translate("MainWindow", "选择文件"))
        self.labe_ip_2.setText(_translate("MainWindow", "路径"))
        self.cbox_customUpload.setText(_translate("MainWindow", "自定义上传"))
        self.tabw_fileUpload.setTabText(self.tabw_fileUpload.indexOf(self.tab_upload), _translate("MainWindow", "文件上传"))
        self.btn_delServer.setText(_translate("MainWindow", "删除"))
        self.lb_base_config.setText(_translate("MainWindow", "基本配置"))
        self.btn_serverConfig.setText(_translate("MainWindow", "配置"))
        self.btn_findServer.setText(_translate("MainWindow", "查询"))
        self.labe_ip_3.setText(_translate("MainWindow", "环境名"))
        self.btn_addServer.setText(_translate("MainWindow", "新增"))
        self.tabw_fileUpload.setTabText(self.tabw_fileUpload.indexOf(self.tab_config), _translate("MainWindow", "项目配置"))
        self.btn_clear.setText(_translate("MainWindow", "清除日志"))
