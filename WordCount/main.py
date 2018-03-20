# coding=utf-8
import sys
import os

RESULT_NAME = 'result.txt'

# 统计字符数
def funChar(flow):
    charLen = len(flow)
    return charLen

# 统计单词
def funWord(flow):
    wordLen = len(flow.replace(',', ' ').split(' '))
    return wordLen
# 统计行数
def funLine(flow):
    lineLen = flow.count('\n') 
    return lineLen + 1

# 写文件
def funOut(result):
    fileObj = open(RESULT_NAME, 'w')
    fileObj.write(result)
    return 0

# 主函数
def main():
    result = ''
    paramsLen = len(sys.argv)
    fileName = sys.argv[paramsLen - 1]
    params = sys.argv[1:-1]
    fileObj = open(fileName, 'r')
    wordFlow = fileObj.read()
    ifOutPut = 0
    for func in params:
        if func == '-c':
            log = '字符数为：' + str(funChar(wordFlow)) + '\n'
            print(log)
            result += log
        if func == '-w':
            log = '单词数为:' + str(funWord(wordFlow)) + '\n'
            print(log)
            result += log
        if func == '-l':
            log = '行数为:' + str(funLine(wordFlow)) + '\n'
            print(log)
            result += log
        if func == '-o':
            ifOutPut = 1            
    if ifOutPut == 1:
        funOut(result)

if __name__ == '__main__':
    main()    