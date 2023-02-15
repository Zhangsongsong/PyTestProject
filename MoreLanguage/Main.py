# !/usr/bin/python

import xlrd
import os

language = {
    '中文': 'values-zh-rCN',
    'English': 'values'
}


def create_dir(path):
    is_exists = os.path.exists(path)
    if not is_exists:
        os.makedirs(path)


source_dir = os.getcwd()

book = xlrd.open_workbook('天天追剧1.2.1.xls')
# 默认第一张表格
firstSheet = book.sheet_by_index(0)
for col in range(1, firstSheet.ncols):
    title = firstSheet.cell_value(0, col)
    # 包名
    packName = language[title]
    absPath = source_dir + "/" + packName
    # 创建目录
    create_dir(absPath)
    print(absPath)
    # 创建strings文件
    strings = absPath + "/strings.xml"
    stringsFile = open(strings, 'w+', encoding='utf-8')
    resources = '<resources>' + '\n'

    # 开始写入
    for row in range(1, firstSheet.nrows):
        resources = resources + '\t' + '<string name="' + firstSheet.cell_value(row, 0) + '">' \
                    + firstSheet.cell_value(row, col) + '</string>' + '\n'
    resources += '</resources>'
    stringsFile.write(resources)
    stringsFile.close()
