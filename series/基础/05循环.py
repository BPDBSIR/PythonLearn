"""
循环
要计算1+2+3我们可以写表达式
"""
print(1 + 2 + 3)

# 要计算 1 + 2 + 3 + ... + 100 勉强也能写出来...

# 但是要计算1 + 2 + 3 + ... + 1000 直接写表达式就不可能了

# 为了让计算机成千上万次的重复运动，我们就需要循环语句

# Python的循环又两种，一种是for..in循环，依次把list或者tuple中每个元素迭代出来
names = ["Andrew", "James", "Mike"]
for name in names:
    print(name)

# 所以for x in ... 循环就是把每个元素带入变量x然后执行缩进块的语句

# 在比如我们像计算1-10的整数之和，我们可以受用sum变量做累加
sux = 0
for x in [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]:
    sux += x
print(sux)

# 如果要计算1-100的整数之和，从1写到100有点空难，幸好Python提供了一个range()函数
# 可以生成一个整数序列，再通过list()函数可以转换为list。比如range(5)生成的序列是从0开始小于5的整数
print(list(range(5)))

# range(101) 就可以生成0-100的整数序列
sux = 0
for i in range(101):
    sux += i
print(sux)
# 看看上面的运行结果，看看结果是不是当年高斯同学心算出的5050


"""
while循环，只要条件满足就不断循环，条件不满足就退出循环
比如我们要计算100以内所有奇数之和，可以使用while循环进行实现
"""
sux = 0
n = 99
while n > 0:
    sux += n
    n -= 2
print(sux)
# 在循环内部变量n不断自减，直到变为-1时，不再满足while条件，循环退出。


# break语句可以提前退出整个循环
# n = 1
# while n <= 100:
#     print(n)
#     n += 1
# print("END")

# 如果想要提前结束循环，可以使用通过break语句
n = 1
while n <= 100:
    if n > 10:
        break
    print(n)
    n += 1
print("END")


# continue跳过当前的这次循环，直接开始下次循环

# 计算100以内所有的偶数和
n = 0
sux = 0
while n <= 100:
    n += 1
    if n % 2 != 0:
        continue
    sux += n
print(sux)

"""
循环是让计算机做重复任务的有效的方法。
break语句可以在循环过程中直接退出循环，而continue语句可以提前结束本轮循环，并直接开始下一轮循环。这两个语句通常都必须配合if语句使用。
要特别注意，不要滥用break和continue语句。break和continue会造成代码执行逻辑分叉过多，容易出错。大多数循环并不需要用到break和continue语句，上面的两个例子，都可以通过改写循环条件或者修改循环逻辑，去掉break和continue语句。
有些时候，如果代码写得有问题，会让程序陷入“死循环”，也就是永远循环下去。这时可以用Ctrl+C退出程序，或者强制结束Python进程。
"""