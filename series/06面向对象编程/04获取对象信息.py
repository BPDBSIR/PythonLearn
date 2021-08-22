"""
获取对象信息
当我们拿到一个对象的引用时，如何知道这个对象是什么类型、有哪些方法呢？

"""

"""
使用type()

首先，我们来判断对象类型，使用type()函数：

基本类型都可以用type()判断：
"""
print(type(213))

print(type("Andrew"))

print(type(12.34))

print(type(True))

print(type(None))

print(type([1, 3, 4]))

print(type((4, 5, 6)))

print(type({"A", "B", "C"}))

print(type({"A": 1, "B": 2, "C": 3}))

# 如果一个变量指向函数或者类，也可以用type()判断...


# 但是type()函数返回的是什么类型呢？它返回对应的Class类型。如果我们要在if语句中判断，就需要比较两个变量的type类型是否相同：
print(type(123) == type(456))

print(type(123) == int)

print(type('abc') == type('123'))

print(type('abc') == str)

print(type('abc') == type(123))

# 判断基本数据类型可以直接写int，str等，但如果要判断一个对象是否是函数怎么办？可以使用types模块中定义的常量：

import types


def fn():
    pass


print(type(fn) == types.FunctionType)

print(type(abs) == types.BuiltinFunctionType)

print(type(lambda x: x) == types.LambdaType)

print(type((x for x in range(10))) == types.GeneratorType)

"""
使用isinstance()
对于class的继承关系来说，使用type()就很不方便。我们要判断class的类型，可以使用isinstance()函数。
>>> isinstance([1, 2, 3], (list, tuple))
True
>>> isinstance((1, 2, 3), (list, tuple))
True

总是优先使用isinstance()判断类型，可以将指定类型及其子类“一网打尽”。

...
"""

"""
使用dir()
如果要获得一个对象的所有属性和方法，可以使用dir()函数，它返回一个包含字符串的list，比如，获得一个str对象的所有属性和方法：
"""
print("Andrew", dir())

# 类似__xxx__的属性和方法在Python中都是有特殊用途的，比如__len__方法返回长度。在Python中，
# 如果你调用len()函数试图获取一个对象的长度，
# 实际上，在len()函数内部，它自动去调用该对象的__len__()方法，所以，下面的代码是等价的：
print(len("ABC"))
print("ABC".__len__())


# 我们自己写的类，如果也想用len(myObj)的话，就自己写一个__len__()方法：
class MyDog(object):

    def __len__(self):
        return 100


dog = MyDog()
print(len(dog))  # 100

# 剩下的都是普通属性或方法，比如lower()返回小写的字符串：
print('ABC'.lower())


class Person(object):

    def __init__(self):
        self.x = 9

    def power(self):
        return self.x * self.x


person = Person()

# 紧接着，可以测试该对象的属性：
print(hasattr(person, "x"))  # 是否有x属性
print(hasattr(person, "y"))  # 是否有y属性

print(setattr(person, "y", 20))  # 设置一个属性y
print(hasattr(person, "y"))  # 是否有y属性

print(getattr(person, "y"))  # 获取属性y

print(person.y)  # 获取属性y

# 如果试图获取不存在的属性，会抛出AttributeError的错误：
# getattr(obj, 'z') # 获取属性'z'

# 可以传入一个default参数，如果属性不存在，就返回默认值：
print(getattr(person, 'z', 404))  # 获取属性'z'，如果不存在，返回默认值404)

# 也可以获得对象的方法：

print(hasattr(person, 'power'))  # 有属性'power'吗？)

print(getattr(person, 'power'))  # 获取属性'power')
