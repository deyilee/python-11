#-*- coding: utf-8 -*-
# 1����������һ���б�����ҳ�xԪ���Ƿ����б����棬������ڷ���1�������ڷ���0

a_list = list(range(20))

def finder(x):
    if x in a_list:
        return 1
    else:
        return 0
        
        
print(finder(10))
print(finder(24))
