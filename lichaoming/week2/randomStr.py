import random
import string

#����Ϊ8���ַ��������
str_length = 8
for i in range(200):
    random_str = ''.join(random.sample(string.ascii_letters + string.digits , str_length))
    print(random_str)