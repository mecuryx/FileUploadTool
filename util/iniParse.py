import configparser
import logging
import re
from PyQt5.QtWidgets import QTableWidgetItem

class INIRWTool:
    def __init__(self):
        self.config = configparser.ConfigParser()
        self.path = '../config/servicesConfig.ini'


    def addSection(self, sectionName):
        try:
            self.config.read(self.path, encoding='UTF-8')
            self.config.add_section(sectionName)
            with open(self.path,"w+", encoding='UTF-8') as f:
                self.config.write(f)
        except Exception as e:
            print(e)

    def getAllSections(self):
        self.config.read(self.path, encoding='UTF-8')
        return self.config.sections()

    def getSectionByInput(self,input):
        results = []
        for section in self.getAllSections():
            if re.search(input,section):
                results.append(section)
        return results
    def delSectionByName(self,sectionName):
        self.config.remove_section(sectionName)
        with open(self.path, "w+", encoding='UTF-8') as f:
            self.config.write(f)

    def getAllServiceName(self,sectionName):
        self.config.read(self.path, encoding='UTF-8')
        return self.config.options(sectionName)

    def addItems(self,sectionName,key,value):
        self.config.read(self.path, encoding='UTF-8')

        self.config.set(sectionName,key,value)
        with open(self.path, "w+", encoding='UTF-8') as f:
            self.config.write(f)


    def getItems(self,sectionName):
        self.config.read(self.path, encoding='UTF-8')
        return self.config.options(sectionName)

    def get(self,sectionName,optionName):
        self.config.read(self.path, encoding='UTF-8')
        return self.config.get(sectionName,optionName)

    def getDataBySection(self, sectionName):
        return self.config.items(sectionName)

    def delete(self, sectionName, optionName ):
        self.config.remove_option(sectionName, optionName)
        with open(self.path, "w+", encoding='UTF-8') as f:
            self.config.write(f)

    def update(self, value):
        pass

if __name__ == '__main__':
    tool = INIRWTool()
    #print(tool.page.sections())
    #tool.page.options('深圳IXP-39')
    #print(tool.addItems("深圳IXP-39",'1','2'))
    tool.addSection("haha")