#��������һ���б�����ҳ�xԪ���Ƿ����б����棬������ڷ���1�������ڷ���0
import re
ss = 'ABCDEFG'
ls = ['A','b','c']
pattern = re.compile('|'.join(ls))
for x in pattern.findall(ss):
    pri


#��һ��Ӣ�ĵĴ��ı��ļ���ͳ�����еĵ��ʳ��ֵĸ�����
import re
def get_word_frequencies(file_name):
    dic = {}
    txt = open(file_name, 'r').read().splitlines()

    n=0
    for line in txt:
        print line
        line = re.sub(r'[.?!,""/]', ' ', line)   
        line = re.sub(r' - ', ' ', line)  
        for word in line.split():

            if word[-1] =='-':
                    m=word[:-1]
                    n=1
                    break
            if n==1:
                word=m+word
                n=0
            print word
            dic.setdefault(word.lower(), 0)  #�����ִ�Сд
            dic[word.lower()] += 1
    #print dic


get_word_frequencies("F:/Export.txt")