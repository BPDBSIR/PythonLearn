"""
面向对象编程基础
活在当下的程序员应该都听说过 面向对象编程 一词
“ 把一组数据结构和处理它们的方法组成对象(object)，把相同行为的对象归纳为类(class)，通过类的封装(encapsulation)隐藏内部细节
  通过继承(inheritance)实现类的特化(specialization)和泛化(generalization)，通过多态(polymorphism)实现基于对象类型的动态分派。
”

"""

"""
定义类
在Python中可以使用class关键字定义类，然后在类中通过之前学习过的函数来定义方法，这样就可以将对象的动态特征描述出花来

"""


class Student(object):

    # __init__是一个特殊方法，用于在创建对象时进行初始化操作
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def study(self, course_name):
        print("%s正在学习%s." % (self.name, course_name))

    def watch_movie(self):
        if self.age < 18:
            print("%s只能观看《熊出没》." % self.name)
        else:
            print("%s正在观看CCTV." % self.name)


""" 说明： 写在类中的函数，我们通常称之为(对象)的方法，这些方法就是对象可以接受的消息 """

"""
创建和使用对象
当我们定义好一个类之后，可以通过下面的方式来创建对象并给对象发消息
"""


def main():
    # 创建学生对象并指定姓名和年龄
    stu1 = Student("Andrew", 19)
    # 调用方法
    stu1.study("Python程序设计")
    stu1.watch_movie()
    stu2 = Student("BPDBSIR", 16)
    stu2.study("小学数学")
    stu2.watch_movie()


if __name__ == "__main__":
    main()

""" 
访问可见性问题
与Java等语言不同的是，Python的可见性只有两种，也就是公开和私有的
如果希望属性是私有的，在给属性命名时可以使用两个下划线作为开头。
"""


class Test:

    def __init__(self, foo):
        self.__foo = foo

    def __bar(self):
        print(self.__foo)
        print("__bar")


def main():
    test = Test("Hello")
    # test.__bar()  # 报错

    # print(test.__foo) # 报错


"""
但是，Python并没有从语法上严格验证私有属性或者方法的私密性，它只是给私有的属性和方法换了一个名字来妨碍对他们的访问
事实上如果你知道跟换名字的规则仍然可以访问他们，之所以这样设定，可以用一句名言加以解释
"We are all consenting adults here " 因为绝大多数程序都认为开放比封闭好，而程序员要自己为自己的行为负责。
"""


class Test2:

    def __init__(self, foo):
        self.__foo = foo

    def __bar(self):
        print(self.__foo)
        print("__bar")


def main():
    test2 = Test2("World")
    test2._Test2__bar()
    print(test2._Test2_foo)


"""
在实际开发中，我们并不建议将属性设置为私有的，因为这回导致子类无法访问，所以大都数Py程序员都会准售一种命名惯例就是让属性名以但下划线开头来标识
属性是受保护的，奔雷之外的代码在访问这样的属性时应该要保持声中，这种做法并不是语法上的规则
但下划线开头的属性和方法外界任然时可以访问的，所以跟多时候它是一种暗示或者隐喻。
"""

"""
面向对象的支柱
面向对象有三大支柱：封装、继承、多态
我们对封装的理解时隐藏一些可以隐藏的实现细节，只向外部暴漏简单的编程接口
我们在类中定义的方法其实就是把数据和对数据的操作封装起来了，我们创建了对象之后，只需要调用对象的方法就可以执行方法中的代码
也就是说我们只需要知道方法的名字传入的参数，而不需要知道方法内部的实现细节
"""

"""
定义一个类描述数字时钟
"""
from time import sleep


class Clock(object):
    """ 数字时钟 """

    def __init__(self, hour=0, minute=0, second=0):
        """
        初始化方法
        :param hour:小时
        :param minute: 分钟
        :param second: 秒
        """

        self._hour = hour
        self._minute = minute
        self._second = second

    def run(self):
        """ 走字 """
        self._second += 1
        if self._second == 60:
            self._second = 0
            self._minute += 1
            if self._minute == 60:
                self._minute = 0
                self._hour += 1
                if self._hour == 24:
                    self._hour = 0

    def show(self):
        """ 显示时间 """
        return '%02d:%02d:%02d' % \
               (self._hour, self._minute, self._second)


def clockFunction():
    clock = Clock(23, 59, 58)
    while True:
        print(clock.show())
        sleep(1)
        clock.run()


# if __name__ == "__main__":
#     clockFunction()


""" 定义一个类描述平面上的点并提供移动点和计算到另一个点距离的方法。 """

from math import sqrt


class Point(object):

    def __init__(self, x=0, y=0):
        """初始化方法

        :param x: 横坐标
        :param y: 纵坐标
        """
        self.x = x
        self.y = y

    def move_to(self, x, y):
        """移动到指定位置

        :param x: 新的横坐标
        "param y: 新的纵坐标
        """
        self.x = x
        self.y = y

    def move_by(self, dx, dy):
        """移动指定的增量

        :param dx: 横坐标的增量
        "param dy: 纵坐标的增量
        """
        self.x += dx
        self.y += dy

    def distance_to(self, other):
        """计算与另一个点的距离

        :param other: 另一个点
        """
        dx = self.x - other.x
        dy = self.y - other.y
        return sqrt(dx ** 2 + dy ** 2)

    def __str__(self):
        return '(%s, %s)' % (str(self.x), str(self.y))


def pointFunction():
    p1 = Point(3, 5)
    p2 = Point()
    print(p1)
    print(p2)
    p2.move_by(-1, 2)
    print(p2)
    print(p1.distance_to(p2))


if __name__ == '__main__':
    pointFunction()

