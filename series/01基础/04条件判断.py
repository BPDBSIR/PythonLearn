"""
条件判断
计算机之所以能够做很多自动化的任务，因为他们可以做条件判断

比如输入用户的年龄，根据年龄打印出不同的内容，在Python中使用if来实现(实际上大多数编程语言都是这么干的)
"""

age = 20
if age >= 18:
    print("Your age is", age)
    print("adult")

# 根据Python 的索引规则，如果if语句判断是True，就把缩进的print语句执行了，否则什么也不做

# 也可以给if添加一个else，意思是，如果if判断是False，不要执行if的呢日哦给，去把else执行了
if age >= 18:
    print("你已经成年!")
else:
    print("你还未成年!")

# 注意不要少写了冒号
# 还可以使用elif做更细致的判断
if age >= 18:
    print("青年")
elif age >= 6:
    print("少年")
else:
    print("儿童")

# elif是else if的缩写，完全可以有多个elif，所以if语句的完整形式就是：
"""
if <条件判断1>:
    <执行1>
elif <条件判断2>:
    <执行2>
elif <条件判断3>:
    <执行3>
else:
    <执行4>
"""

# if判断条件还可以简写，比如写：
x = 12

if x:
    print("True")

# 只要x时候非零数值、非空字符串、非空list等，就判断为True 否则为False


"""
input
键盘录入
"""
# 使用input()读取 用户的输入，这样可以自己输入，程序运行的很有意思
# birth = input("birth: ")
# if birth < 2000:
#     print("00前")
# else:
#     print("00后")

"""
输入1982，结果报错：
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: unorderable types: str() > int()

"""

# 这是因为input()返回的数据类型是str，str不饿能直接和整数进行比较，必须先把str转换为整数
# Python提供了int()函数来完成这件事情
birth = int(input("birth: "))
if birth < 2000:
    print("00前")
else:
    print("00后")