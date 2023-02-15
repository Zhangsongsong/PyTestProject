# !/usr/bin/python

import os
import xlrd
from xlutils import copy

absFile = os.getcwd() + '/strings.xml'

xlsFile = os.getcwd() + '/天天追剧1.2.1.xls'

book = xlrd.open_workbook(xlsFile)
newBook = copy.copy(book)
sheet = newBook.get_sheet(0)

lines = open(absFile)
index = 0
for line in lines:
    content = line.lstrip()
    if content.startswith('<string name='):
        index = index + 1
        keys = content.split('"')

        startIndex = keys[2].find('>')
        endIndex = keys[2].find('</string>')
        print(keys[1], keys, startIndex, endIndex, "字符串截取：", keys[2][startIndex + 1: endIndex])
        sheet.write(index, 0, keys[1])
        sheet.write(index, 1, keys[2][startIndex + 1: endIndex])
lines.close()
newBook.save('new.xls')
