#打印斐波那契数列前100项，测试上传
#first
a,b=0,1
for i in range(102):
    if b<=100:
        print(b,end=",")
        a,b=b,a+b
#second
a,b=0,1
while b<100:
    print(b,end=",")
    a,b=b,a+b
