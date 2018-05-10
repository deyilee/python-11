#-*- coding: utf-8 -*-
#��һ��Ӣ�ĵĴ��ı��ļ���ͳ�����еĵ��ʳ��ֵĸ���

import os

word_count = {}
with open('english_articles') as f:
    words = f.readline().split()
    #print(words)
    for w in words:
        word_end_with = [',', '.', '!', ':', ';']
        for s in word_end_with:
            if w.endswith(s):
                w = w.split(s)[0]
        if not w in word_count:
            word_count[w] = 1
        else:
            word_count[w] +=1
            
for k, v in word_count.items():
    print('{0} count: {1}'.format(k, v))
    