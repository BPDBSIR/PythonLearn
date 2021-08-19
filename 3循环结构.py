from math import sqrt

"""
循环结构
在我们写程序的时候，一定会遇到徐娅哦重复执行某条或者某些指令的场景。例如程序控制机器人踢足球
如果机器人只求而且还没有进入射门范围，那么我们就需要一直发出让 机器人向球门方向移动的指令。
在这个场景中，让机器人向球门方向移动就是一个需要重复的动作，

循环结构就是程序中控制某条或者某些只指令重复执行的机构
在Python中构造循环结构有两种做法，一种是for-in循环，一种是while循环。
"""
import random

"""
for-in循环
如果明确知道执行的次数或者要对一个容器进行迭代，那么推荐for-in的方式进行循环
"""
num = 0
for x in range(101):
    num += x
print(num)

"""
上面的代码中的range(1,101)可以用来构造一个从1到100的烦恼为，当我们把这样一个范围方位for-in循环中
就可以通过过前面的循环变量x依次去除1到100的整数，当然，range的用法非常灵活
    range(101)：可以用来产生0到100范围的整数，需要注意的是取不到101
    range(1,101)：可以用来产生1到100范围额整数，相当于前面是闭区间后面的开区间
    range(1,101,2)：可以用来产生1到100的奇数，其中2是步长，即每次数值递增的值
    range(100,0,-2)：可以用来产生100到1的偶数，其中-2是步长，即每次数字递减的值
"""

"""
知道了以上的字知识，我们求出1-100之间的偶数和
"""
num = 0
for x in range(2, 101, 2):
    num += x
print(num)

"""
当然也可以通过循环体中使用分支结构的方式来实现相同的功能
"""
num = 0
for x in range(1, 101):
    if x % 2 == 0:
        num += x
print(num)

"""
while循环
如果要构造不知道具体循环次数的循环结构，我们推荐使用while循环。
while循环通过一个能够产生或者转换出bool值的表达式来控制循环，表达式的值为True则继续循环，为False则结束循环

下面通过一个猜数字的小游戏来看看如何使用while循环，猜数字的游戏规则是：
计算机出一个1到100之间的随机数，玩家输入自己猜的数字，计算机给出对应的提示信息(大一点、小雨点或者猜对了)
如果顽疾猜中了数字，计算机提示用户一共猜了都偶稍次，游戏结束，否则游戏继续。
"""
answer = random.randint(1, 100)
counter = 0
while True:
    counter += 1
    number = int(input("请输入: "))
    if number < answer:
        print("大一点")
    elif number > answer:
        print("小一点")
    else:
        print("恭喜你猜对了!")
        break
print("你总共猜了%d次" % counter)
if counter > 7:
    print("你的智商余额明显不足!")
""" 
需要注意的是break用来终止循环
且只能终止它所在的那个循环
除了break之外，还有另外一个关键字是continue，它可以用来放弃本次循环后续的代码直接让循环进入下一轮。

和分支结构一样，循环结构也是可以嵌套的，也就是说在循环中还可以构造循环结构。
"""

for i in range(1, 10):
    for j in range(1, i + 1):
        print("%d*%d=%d" % (i, j, i * j), end="\t")
    print()

"""
判断一个数是否为素数
提示：素数指的是只能被1和自身整除的大于1的整数。
"""

num = int(input("请输入一个整数: "))
end = int(sqrt(num))
is_prime = True
for x in range(2, end + 1):
    if num % x == 0:
        is_prime = False
        break
if is_prime and num != 1:
    print("%d是素数" % num)
else:
    print("%d不是素数" % num)

"""
输入两个正整数，计算它们的最大公约数和最小公倍数。
提示：两个数的最大公约数是两个数的公共因子中最大的那个数；两个数的最小公倍数则是能够同时被两个数整除的最小的那个数。
"""
x = int(input('x = '))
y = int(input('y = '))
# 如果x大于y就交换x和y的值
if x > y:
    # 通过下面的操作将y的值赋给x, 将x的值赋给y
    x, y = y, x
# 从两个数中较的数开始做递减的循环
for factor in range(x, 0, -1):
    if x % factor == 0 and y % factor == 0:
        print('%d和%d的最大公约数是%d' % (x, y, factor))
        print('%d和%d的最小公倍数是%d' % (x, y, x * y // factor))
        break


"""
打印如下所示的三角形图案

*
**
***
****
*****

    *
   **
  ***
 ****
*****

    *
   ***
  *****
 *******
*********

"""

row = int(input('请输入行数: '))
for i in range(row):
    for _ in range(i + 1):
        print('*', end='')
    print()


for i in range(row):
    for j in range(row):
        if j < row - i - 1:
            print(' ', end='')
        else:
            print('*', end='')
    print()

for i in range(row):
    for _ in range(row - i - 1):
        print(' ', end='')
    for _ in range(2 * i + 1):
        print('*', end='')
    print()
