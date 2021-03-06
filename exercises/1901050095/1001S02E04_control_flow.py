#使用for......in循环打印九九乘法口诀表
i = 1   #因为下一行有数集左开始为1，所以这一行初始赋值可以省略
for i in range(1,10):   #for循环，函数range()提供一个数集，让i在数集中迭代
    for j in range(1,i+1):  
        print(i,"*",j,"=",i*j,sep='',end='\t')
        #print()函数，默认屏幕输出，sep字符间隔0个空格(默认间隔1空格),end结束间隔，'\t'一个制表位
    print()     #无参数即默认换行符\n
print()     #结束本模块换行

####################################################################

#使用while循环打印九九乘法口诀表
i = 1    #初始赋值语句，让变量i从1开始；与for循环不同，while无初始值，所以这一行不能省略
while i <= 9:   #while循环，用表达式让变量从1到9迭代
    j = 1
    while j <= i:   #j的取值受i控制
        print(i,"*",j,"=",i*j,end='\t')  #无sep参数，默认字符间隔1个空格
        j += 1  #在i取值范围内，j+1步长实现迭代
    print()     #一行结束换行  
    i += 1     #i+1步长进行循环下一行,for循环不需要
print()     #结束本模块换行

####################################################################

#使用while循环打印九九乘法口诀表，并用break和continue去掉偶数行
i = 1    #初始赋值语句，让变量i从1开始
while i <= 9:   #while循环，用表达式让变量从1到9迭代
    j = 1
    while j <= i:   #j的取值受i控制
        if i % 2 == 0:      #条件判断偶数行
            break       #break用于跳出最近的for或while循环
        print(i,'*',j,"=",i*j,end='    ')     #单双引号相同
        j += 1  #在i取值范围内，j+1步长实现迭代
    print()     #一行结束，换行;偶数行它也要执行，现在还没找到原因把它去掉
    i += 1    #i+1步长进行循环下一行
print()     #结束本模块换行
