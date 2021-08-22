"""
迭代
如果给定一个list或者tuple，我们可以通过for循环来遍历这个list或者tuple，这种遍历我们称之为迭代

在Python中，迭代是通过for...in来完成的，而很多语言对比C语言，迭代list是通过下表完成的
比如以下c代码：
for(i = 0; i < length; i++){
    n = list[i]
}

可以看的出，Python的for循环抽象程度要高于C的for循环，因为Python虚拟换不仅可以用整改list或者tuple上，还可以作用于在其他可迭代对象上

list这种数据类型虽然有下标，但是很多其他数据类型是没有下标的，但是，只要是可迭代对象，无论有没有下标，都可以迭代，比如dict就可以迭代
"""
d = {"A": 1, "B": 2, "C": 3}
for key in d:
    print(key)

# 因为dict的储存不是按照list的方式进行存储的，所以，迭代出的结果顺序很可能不一样
# 默认情况下，dict迭代的是key，如果要迭代value，可以使用for value in d.values()，如果要同时迭代key和value，可以使用for k,v in d.items()

# 由于字符串也是可迭代对象，英雌也可以用于for循环
for ch in "ABCD":
    print(ch)

# 所以当我们使用for循环的时候，只要作用于一个可迭代对象，for循环就可以正常运行，而我们不太关心对象究竟是list还是其他数据类型

# 那么，如果判断一个对象是否为可迭代对象呢？方法是通过collections.abc模块的Iterable类型判断
from collections.abc import Iterable

# 判断str是否可以迭代
print(isinstance("abc", Iterable))

# 判断list是否可以迭代
print(isinstance([1, 2, 3], Iterable))

# 判断整数是否可以迭代
print(isinstance(123, Iterable))

# 如果要对list实现雷士Java那样的下标循环怎么办？Python内置了enumerate函数可以把list编程索引-元素对，这样就可以在for循环中同时迭代索引和元素本身
for i, value in enumerate(["A", "B", "C"]):
    print(i, value)

# 上面的for循环里，同时引用了两个变量，在Python里是很常见的，比如下面的代码：
for x, y in [(1, 1), (2, 4), (3, 9)]:
    print(x, y)

