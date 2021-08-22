"""

函数的参数

定义函数的时候，我们把参数的名字和位置确定下来，函数的接口定义就完成了。对于函数的调用者来说，只需要知道如何传递正确的参数
以及函数将返回什么样的值就够了，函数内部的复杂逻辑被封装起来，调用者无需了解。

Python的函数定义非常简单，但灵活度却非常大。除了正常定义的必选参数外，还可以使用默认参数、可变参数和关键字参数，使得函数定义出来的接口，不但能处理复杂的参数，还可以简化调用者的代码。

"""


# 位置参数
def power(x):
    return x * x


# 对于power(x)函数，x就是一个位置参数

# 当我们调用power函数时，必须传入有且仅有的一个参数x：
power(5)


# 现在，如果我们要计算x3怎么办？可以再定义一个power3函数，但是如果要计算x4、x5……怎么办？我们不可能定义无限多个函数。

# 你也许想到了，可以把power(x)修改为power(x, n)，用来计算xn，说干就干：

def power(x, n):
    s = 1
    while n > 0:
        n = n - 1
        s = s * x
    return s


# 对于这个修改后的power(x, n)函数，可以计算任意n次方：

power(5, 2)


# 修改后的power(x, n)函数有两个参数：x和n，这两个参数都是位置参数，调用函数时，传入的两个值按照位置顺序依次赋给参数x和n。

# 默认参数
# 新的power(x, n)函数定义没有问题，但是，旧的调用代码失败了，原因是我们增加了一个参数，导致旧的代码因为缺少一个参数而无法正常调用：
# power(5)
# Python的错误信息很明确：调用函数power()缺少了一个位置参数n。


# 这个时候，默认参数就排上用场了。由于我们经常计算x2，所以，完全可以把第二个参数n的默认值设定为2：
def power(x, n=2):
    s = 1
    while n > 0:
        n = n - 1
        s = s * x
    return s


# 这样，当我们调用power(5)时，相当于调用power(5, 2)：
power(5)


# 一是必选参数在前，默认参数在后，否则Python的解释器会报错（思考一下为什么默认参数不能放在必选参数前面）；
# 二是如何设置默认参数。
# 当函数有多个参数时，把变化大的参数放前面，变化小的参数放后面。变化小的参数就可以作为默认参数。
# 使用默认参数有什么好处？最大的好处是能降低调用函数的难度。
# 举个例子，我们写个一年级小学生注册的函数，需要传入name和gender两个参数：
def enroll(name, gender):
    print('name:', name)
    print('gender:', gender)


# 这样，调用enroll()函数只需要传入两个参数：
enroll('Sarah', 'F')


# 如果要继续传入年龄、城市等信息怎么办？这样会使得调用函数的复杂度大大增加。
# 我们可以把年龄和城市设为默认参数：
def enroll(name, gender, age=6, city='Beijing'):
    print('name:', name)
    print('gender:', gender)
    print('age:', age)
    print('city:', city)


# 这样，大多数学生注册时不需要提供年龄和城市，只提供必须的两个参数：
enroll('Sarah', 'F')

# 只有与默认参数不符的学生才需要提供额外的信息：
enroll('Bob', 'M', 7)
enroll('Adam', 'M', city='Tianjin')


# 默认参数很有用，但是如果使用不当，也会掉进坑里面，默认参数有两个最大的坑，先行医一个函数，传入一个list，添加一个END在返回
def add_end(L=[]):
    L.append("END")
    return L


# 当你正常调用的时候，结果似乎不会报错
print(add_end([1, 2, 3]))

print(add_end(['x', 'y', 'z']))

# 当你使用默认参数调用的时候，一开始结果也是对的
print(add_end())

# 但是再次调用add_end()的时候，结果就不对了
print(add_end())


# 很多初学者很疑惑，默认参数是[]，但是函数似乎每次都“记住了”上次添加了'END'后的list。

# 这是因为，Python函数在定义的时候，默认参数L的值就被计算出来了，即[]，因为默认参数L也是一个变量，它指向对象[]，每次调用该函数，如果改变了L的内容，
# 默认参数的内容就变了，不再是函数定义时的[]了。
# 定义默认参数要牢记一点：默认参数必须指向不变对象！

# 要修改上面的例子，我们可以用None这个不变对象来实现：
def add_end(L=None):
    if L is None:
        L = []
    L.append('END')
    return L


# 现在，无论调用多少次，都不会有问题：
print(add_end())

print(add_end())

# 为什么要设计str、None这样的不可变对象呢？因为不变对象一旦创建，对象内部的数据就不能修改，这样就减少了由于修改数据导致的错误
# 此外，由于对象不变，多任务环境下同时读取对象不需要加锁，同时读一点问题都没有，我们在编写程序的似乎后，如果可以设计一个不可变对象，那就尽量少设计成不可变对象。


"""
可变参数
在Python函数中，还可以定义可变参数。顾名思义，可变参数就是传入的参数个数是可变的，可以是1个、2个到任意个，还可以是0个。
我们以数学题为例子，给定一组数字a，b，c……，请计算a2 + b2 + c2 +
要定义出这个函数，我们必须确定输入的参数。由于参数个数不确定，我们首先想到可以把a，b，c……作为一个list或tuple传进来，这样，函数可以定义如下：
"""


def calc(numbers):
    sum = 0
    for n in numbers:
        sum = sum + n * n
    return sum


# 但是调用的时候，需要先组装出一个list或tuple：

print(calc([1, 2, 3]))


# 如果利用可变参数，调用函数的方式可以简化成这样： print(calc(1,2,3))

# 所以，我们把函数的参数改为可变参数：
def calc(*numbers):
    sum = 0
    for n in numbers:
        sum = sum + n * n
    return sum


# 定义可变参数和定义一个list或tuple参数相比，仅仅在参数前面加了一个*号。
# 在函数内部，参数numbers接收到的是一个tuple，因此，函数代码完全不变。但是，调用该函数时，可以传入任意个参数，包括0个参数：
print(calc(1, 2))
print(calc())

# 如果已经有一个list或者tuple，要调用一个可变参数怎么办？可以这样做：

nums = [1, 2, 3]
print(calc(nums[0], nums[1], nums[2]))

# 这种写法当然是可行的，问题是太繁琐，所以Python允许你在list或tuple前面加一个*号，把list或tuple的元素变成可变参数传进去：

nums = [1, 2, 3]
print(calc(*nums))

# *nums表示把nums这个list的所有元素作为可变参数传进去。这种写法相当有用，而且很常见。


"""
关键字参数
可变参数允许你传入0个或者任意个函数，这些可变参数在函数调用的时候自动组装为一个tuple。而关键字参数允许你传入0个或者任意个参数名的参数，这些关键字
参数在函数的内部自动组装为一个dict。
"""


def person(name, age, **kw):
    print("name:", name, "age:", age, "other:", kw)


person("Andrew", 20)

# 函数person除了必选参数name和age以外，还接受关键字参数kw，在调用该函数时，可以只传入必选参数
person("BJZ", 19)

# 也可以传入任意个数的关键字参数
person('Adam', 45, gender='M', job='Engineer')

# 关键字参数有什么用？它可以扩展函数的功能。比如，在person函数里，我们保证能接收到name和age这两个参数，但是，如果调用者愿意提供更多的参数，我们也能收到。
# 试想你正在做一个用户注册的功能，除了用户名和年龄是必填项外，其他都是可选项，利用关键字参数来定义这个函数就能满足注册的需求。

# 和可变参数类型，也可以先组成出一个dict，然后把该dict转换为关键字参数传进去
extra = {"city": "Henan", "hobby": "BasketBall"}

person("BJZ", 20, city=extra["city"], hobby=extra["hobby"])

# 当然，上面复杂的调用也可以简化
person("Jack", 24, **extra)

# **extra表示把extra这个dict的所有key-value用关键字参数传入到函数的**kw参数
# kw将获得一个dict，注意kw获得的dict是extra的一份拷贝，对kw的改动不会影响到函数外的extra。


"""
命名关键字参数
对于关键字参数，函数的调用者可以传入任意不受限制的关键字参数。至于到底传入了哪些，就需要在函数内部通过kw检查。
仍以person()函数为例，我们希望检查是否有city和job参数：
"""


def person(name, age, **kw):
    if 'city' in kw:
        # 有city参数
        pass
    if 'job' in kw:
        # 有job参数
        pass
    print('name:', name, 'age:', age, 'other:', kw)


person('Jack', 24, city='Beijing', addr='Chaoyang', zipcode=123456)


# 如果要限制关键字参数的名字，就可以用命名关键字参数，例如，只接收city和job作为关键字参数。这种方式定义的函数如下：
def person(name, age, *, city, job):
    print(name, age, city, job)


# 和关键字参数**kw不同，命名关键字参数需要一个特殊分隔符*，*后面的参数被视为命名关键字参数。
person("Mike", 20, city="NewYork", job="Engineer")


# 如果函数定义中已经有了一个可变参数，后面跟着的命名关键字参数就不再需要一个特殊分隔符*了：
def person(name, age, *args, city, job):
    print(name, age, args, city, job)


# 命名关键字参数必须传入参数名，这和位置参数不同。如果没有传入参数名，调用将报错：
"""
person('Jack', 24, 'Beijing', 'Engineer')
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: person() missing 2 required keyword-only arguments: 'city' and 'job'
"""


# 由于调用时缺少参数名city和job，Python解释器把前两个参数视为位置参数，后两个参数传给*args，但缺少命名关键字参数导致报错。
# 命名关键字参数可以有缺省值，从而简化调用：
def person(name, age, *, city='Beijing', job):
    print(name, age, city, job)


# 由于命名关键字参数city具有默认值，调用时，可不传入city参数：
person('Jack', 24, job='Engineer')


# 使用命名关键字参数时，要特别注意，如果没有可变参数，就必须加一个*作为特殊分隔符。如果缺少*，Python解释器将无法识别位置参数和命名关键字参数：
def person(name, age, city, job):
    # 缺少 *，city和job被视为位置参数
    pass


"""
参数组合
在Python中定义函数，可以用必选参数、默认参数、可变参数、关键字参数和命名关键字参数，这5种参数都可以组合使用。但是请注意，参数定义的顺序必须是：必选参数、默认参数、可变参数、命名关键字参数和关键字参数。
比如定义一个函数，包含上述若干种参数：
"""


def f1(a, b, c=0, *args, **kw):
    print('a =', a, 'b =', b, 'c =', c, 'args =', args, 'kw =', kw)


def f2(a, b, c=0, *, d, **kw):
    print('a =', a, 'b =', b, 'c =', c, 'd =', d, 'kw =', kw)


# 在函数调用的时候，Python解释器自动按照参数位置和参数名把对应的参数传进去。

f1(1, 2)
f1(1, 2, c=3)
f1(1, 2, 3, 'a', 'b')
f1(1, 2, 3, 'a', 'b', x=99)
f2(1, 2, d=99, ext=None)

# 最神奇的是通过一个tuple和dict，你也可以调用上述函数：
args = (1, 2, 3, 4)
kw = {'d': 99, 'x': '#'}
f1(*args, **kw)
args = (1, 2, 3)
kw = {'d': 88, 'x': '#'}
f2(*args, **kw)
