from main import funChar,funWord,funLine,funOut,main
import os

TEST_DIR = './test/'
RESPECT_RESULTS_CHAR = [14,32,63,13,12,13,16,35,14,19]
RESPECT_RESULTS_WORD = [4,4,20,6,3,4,5,5,6,3]
RESPECT_RESULTS_LINE = [1,7,10,1,1,1,2,3,1,2]

def test():
    fileNames = os.listdir(TEST_DIR)
    result = ''
    passLine = 0
    passWord = 0
    passChar = 0
    i = 0
    for fileName in fileNames:
        fileOj = open(TEST_DIR + fileName, 'r')
        wordFlow = fileOj.read()
        resultLine = funLine(wordFlow)
        resultWord = funWord(wordFlow)
        resultChar = funChar(wordFlow)
        if resultLine == RESPECT_RESULTS_LINE[i]:
            passLine += 1
        if resultWord == RESPECT_RESULTS_WORD[i]:
            passWord += 1
        if resultChar == RESPECT_RESULTS_CHAR[i]:
            passChar += 1
        print('Test Cases:' + fileName)
        i += 1
    print('Test Result: Total ' + str(len(fileNames)))
    print('PassLine: ' + str(passLine))
    print('PassWord: ' + str(passWord))
    print('PassChar: ' + str(passChar))    
    return 0

if __name__ == '__main__':
    test()