import logging
import os
import logging.handlers
import sys
import mmm
import re

import sys
# -*- coding: utf-8 -*-

class log():
    def __init__(self):#每次都会执行的
        self.logger = logging.getLogger()
        #self.cur_path = os.path.dirname(os.path.abspath(sys.argv[0]))#当前脚本的绝对位置
        self.filename=mmm.mulu()
        #print(self.filename)
       # self.filename=r'C:\Users\Administrator\PycharmProjects\untitled8/log/text.txt'
        self.logger.setLevel(level = logging.INFO)
        '''self.handler= logging.handlers.RotatingFileHandler(filename=self.filename, maxBytes=20, backupCount=5)#
         按文件大小，不太好，换称日期型的'''
        self.handler=logging.handlers.TimedRotatingFileHandler(filename=self.filename, when="D", interval=1, backupCount=7,encoding='utf8')# when="D", interval=1每天产生一个日志文件 encoding='utf8'保证日志的输出文件内容不乱码
        #self.handler.suffix="%Y-%m-%d_%H-%M.log"
        #self.handler.extMatch=re.compile(r"^\d{4}-\d{2}-\d{2}_\d{2}-\d{2}.log$")
        #文件日志
        #self.handler = logging.FileHandler("log.txt")#日志名称
        #self.handler= logging.FileHandler(filename='test.log', encoding='gbk')
        self.formatter = logging.Formatter('%(asctime)s - %(filename)s - %(name)s - %(levelname)s: - %(message)s')
        self.handler.setFormatter(self.formatter)#日志输出格式
        self.handler.setLevel(logging.INFO)#指定日志最低输出级别

        #logging.config.fileConfig('logging.conf')
        self.console = logging.StreamHandler()
        self.console.setLevel(logging.INFO)

        self.logger.addHandler(self.handler)
        self.logger.addHandler(self.console)

    def  info(self,msg):#s.decode('gbk','ignore').encode('utf-8′)
        self.logger.info(msg)
    def debug(self,msg):
        self.logger.debug(msg)
    def warning(self,msg):
        self.logger.warn(msg)
    def error(self,msg):
        self.logger.error(msg)
#logger.info("Start print log")
#logger.debug("Do something")
#logger.warning("Something maybe fail.")
#logger.info("Finish")
if __name__ == '__main__':
    a=log()
    print(a.debug('我是神'))