#local��global��shell�ַ�ʽ����
#pyenv global �޸�ϵͳȫ�ֵ�Python����
#pyenv local  �޸ĵ�ǰĿ¼��Python����
#pyenv shell  �޸ĵ�ǰshell��Python��������ʱ����ǰϵͳ�͵�ǰĿ¼���趨��Python�汾���ᱻ���ԡ�
#             �����´�һ���µ�shell�󣬸û���Ҳ��ʧЧ��

#��ӡ��100���ڵ�쳲���������
a = 0
b = 1
while b < 100:
    print(b)
    a, b = b, a+b

#��ӡ��100���ڵ�쳲���������
fibs = [0,1]
for i in range(10):
    fibs.append(fibs[-2] + fibs[-1])
fibs

#ʹ�� Python ʵ��������� 200 ���ظ������루�����Ż�ȯ�����ַ������ȴ���5����
import random  
str = ''  
randomdict = {}  
char = 'AaBbCcDdEeFfGgHhIiJjKkLlMmNnOoPpQqRrSsTtUuVvWwXxYyZz0123456789'  
length = len(char)  
for keys in range(200):  
    for v in range(5):  
         str += random.choice(char) 
    randomdict[keys] = str  
    str = ''  
print(randomdict)  