#!/usr/bin/python
#coding:utf8
'''
Factory Method
'''
'''
class ChinaGetter:
    """A simple localizer a la gettext"""
    def __init__(self):
        self.trans = dict(dog=u"小狗", cat=u"小猫")
        print(self.trans)

    def get(self, msgid):
        """We'll punt if we don't have a translation"""
        try:
          print( self.trans[msgid])
          return self.trans[msgid]
        except KeyError:#没有这个键
           return str(msgid)


class EnglishGetter:
    """Simply echoes the msg ids"""
    def get(self, msgid):
        return str(msgid)


def get_localizer(language="English"):
    """The factory method"""
    languages = dict(English=EnglishGetter, China=ChinaGetter)
    print(languages)
    return languages[language]()

# Create our localizers
e, g = get_localizer("English"), get_localizer("China")
# Localize some text
print(e)
for msgid in "dog parrot cat bear".split():
    print(e.get(msgid), g.get(msgid))'''


# _*_coding=UTF-8_*_
# 使用自定义异常类实现指定输入字符串长度
# 自定义异常类
class SomeCustomError(Exception):
    def __init__(self, str_length):
        super(SomeCustomError, self).__init__()
        self.str_length = str_length


# 使用自定义异常



