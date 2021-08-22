"""
定义函数

格式：
def  函数名(参数列表):
    函数体
    return 返回值
"""


# 空函数
# 如果想定义遗憾什么事情也不做的空函数，可以使用pass语句
def nop():
    pass


# pass语句什么也不做，哪有什么作用呢？实际上pass可以用来作为占位符，比如现在还没想好怎么写函数的代码，就可以先放一个pass，让代码能运行起来，否则会报错

# pass还可以加在其他语句里面
age = 20
if age >= 18:
    pass

# 如果缺少了pass，代码运行就会有错误提示

# 参数检查
# 调用函数时，如果参数个数不对，Python解释器会抛出TypeError异常

# 如果参数化类型不匹配，Python解释器就无法帮我们检查


# 返回多个值
# 比如在游戏中进场需要从一个点移动到另外一个点，给出坐标，唯一和角度，就可以计算出新的坐标

import math


def move(x, y, step, angle=0.0):
    nx = x + step * math.cos(angle)
    ny = y - step * math.sin(angle)
    return nx, ny


if __name__ == '__main__':
    r = move(100, 100, 60, math.pi / 6)
    print(r)

# 但其实这只是一种假象，Python函数返回的仍然是单一值：

# 原来返回值是一个tuple！但是，在语法上，返回一个tuple可以省略括号，而多个变量可以同时接收一个tuple，按位置赋给对应的值，所以，Python的函数返回多值其实就是返回一个tuple，但写起来更方便。


"""
定义函数时，需要确定函数名和参数个数；

如果有必要，可以先对参数的数据类型做检查；

函数体内部可以用return随时返回函数结果；

函数执行完毕也没有return语句时，自动return None。

函数可以同时返回多个值，但其实就是一个tuple。
"""
