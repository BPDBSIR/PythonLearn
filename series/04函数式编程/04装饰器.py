"""
装饰器
由于函数也是一个对象，而且函数对象可以被赋值给变量，所以，通过变量也能调用该函数
"""


def now():
    print("2021-08-22")


f = now
print(f())

# 函数对象有一个__name__属性，可以拿到函数的名字
print(now.__name__)


# 现在，假设我们要增强now()函数的功能，比如在函数调用前后自动打印日志，但是又不希望修改now()函数的定义，这种代码运行期间动态增加功能的方式，就称为装饰器(Decorator)

# 本质上，Drcorator就是一个返回函数的高阶函数，所以，我们定义一个能打印日志的Decorator
def log(func):
    def wrapper(*args, **kw):
        print("call %s(): " % func.__name__)
        return func(*args, **kw)

    return wrapper


# 观察上面的log，因为它是一个Decorator，所以接收一个函数作为参数，并返回一个函数，我们要借助Python的@语法，把Decorator置于函数的定义处


@log
def now():
    print("2021-08-22")


# 调用now()函数，不仅会运行now()函数本身，还会在运行now()函数前面打印一行日志
now()

# 把@log放到now()函数的定义处，相当于执行了语句
now = log(now)

"""
由于log()是一个装饰器，返回一个函数，所以，原来的now()函数仍然存在，只是现在同名的函now变量指向了新的函数
于是调用now()将执行新函数，即在log()函数中返回wrapper()函数。

wrapper()函数的参数定义是(*args,**kw)，英雌wrapper()函数可以接收任意参数的调用，在wrapper()函数内，首先打印日志，在紧接着调用原始函数

"""


# 如果decorator本身需要传入参数，那就需要编写一个返回decorator的高阶函数，写出来会更复杂。比如，要自定义log的文本：

def log(text):
    def decorator(func):
        def wrapper(*args, **kw):
            print("%s %s(): " % (text, func.__name__))
            return func(*args, **kw)

        return wrapper

    return decorator


# 这个3层嵌套的decorator用法如下：
@log('execute')
def now():
    print('2015-3-25')


now()

# 和两层嵌套的decorator相比，3层嵌套的效果是这样的
now = log("execute")(now)

"""
首先执行log('execute')，返回的是decorator函数，再调用返回的函数，参数是now函数，返回值最终是wrapper函数

以上两种decorator的定义都没有问题，但是还差一步，因为函数是对象，它有__name__等属性
但你取看经过decorator钻杆是的函数，他们的__name__已经从原来的"now"变成了"wrapper"
"""
print(now.__name__)

# 因为返回的那个wrapper()函数名字就是wrapper，所以需要把原始函数的__name__等属性复制到wrapper()函数中，否则，有些依赖函数签名的代码执行就会出错。

# 不需要编写wrapper.__name__ = func.__name__这样的代码，Python内置的functools.wraps就是干这个事的，所以，一个完整的decorator的写法如下：
import functools


def log(func):
    @functools.wraps(func)
    def wrapper(*args, **kw):
        print('call %s():' % func.__name__)
        return func(*args, **kw)

    return wrapper


# 或者针对带参数的decorator：
def log(text):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kw):
            print('%s %s():' % (text, func.__name__))
            return func(*args, **kw)

        return wrapper

    return decorator

# import functools是导入functools模块。现在，只需记住在定义wrapper()的前面加上@functools.wraps(func)即可。
