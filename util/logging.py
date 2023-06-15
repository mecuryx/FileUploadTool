import datetime
from PyQt5.QtWidgets import QTextBrowser as qb


class Log:
    def __init__(self, qb):
        self.qb = qb

    def printLog(self, content):
        now = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        self.qb.append(now + ":" + content)

    def clearLog(self):
        self.qb.clear()
