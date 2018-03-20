# coding=utf-8
import sys
import os

RESULT_NAME = 'result.txt'

# 统计字符数
def funChar(flow):
    charLen = len(flow)
    result = '字符数为：' + str(charLen) + '\n'
    print(result)
    return result

# 统计单词
def funWord(flow):
    wordLen = len(flow.replace(',', ' ').split(' '))
    result = '单词数为:' + str(wordLen) + '\n'
    print(result)
    return result
# 统计行数
def funLine(flow):
    lineLen = flow.count('\n')
    result = '行数为:' + str(lineLen) + '\n'
    print(result)
    return result

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
            result += funChar(wordFlow)
        if func == '-w':
            result += funWord(wordFlow)
        if func == '-l':
            result += funLine(wordFlow)
        if func == '-o':
            ifOutPut += 1            
    if ifOutPut == 1:
        funOut(result)

main()    