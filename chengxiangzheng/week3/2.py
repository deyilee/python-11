#cxz.txt 位于当前目录下,当前用户python。
import re
def get_word_num(place):
    with open(place,'r')as f: #打开文件，记作f
        data = f.read()
    result = re.split(r"[^a-zA-Z]",data) #split分割字符串，用正则公式匹配
    # print(data)
    print (len([x for x in result if x!= ''])) #输出单词数，历遍一次，不等于空格

if __name__ == "__main__":
    get_word_num('cxz.txt')
