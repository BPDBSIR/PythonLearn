"""
面向对象进阶


@property装饰器
我们虽然不建议将属性设置为私有的，但是如果直接将属性暴漏给外界也是没有问题的，比如我们没有办法检查赋值属性的值是否有效
我们之前建议的是将属性命名以单下划线开头，通过这种方式阿里暗示是属性受保护的，不建议外界直接访问，那么如果向访问属性可以直接通过属性的
getter(访问器)和setter(修改器)方法进行对应的操作，
如果要做到这一点，就可以考虑使用@property包装器来包装getter和setter方法，使用对属性的访问即安全又方便

"""


class Person(object):

    def __init__(self, name, age):
        self._name = name
        self._age = age

    # getter
    @property
    def name(self):
        return self._name

    # getter
    @property
    def age(self):
        return self.age

    # setter
    @age.setter
    def age(self, age):
        self._age = age

    def play(self):
        if self._age <= 16:
            print("%s正在玩飞行棋." % self._name)
        else:
            print("%s正在斗地主." % self._name)


def main():
    person = Person("Andrew", 12)
    person.play()
    person.age = 22
    # person.name = "BPDBSIR"  # AttributeError: can't set attribute
    person.play()


if __name__ == "__main__":
    main()

"""
__slots__魔法
Python是一门动态语言，通常，动态语言允许我们在程序运行是给对象绑定新的属性和方法，当然也可以对已经绑定好的属性和方法进行解绑
但是如果我们需要限定自定义类型的对象只能绑定某些属性，可以通过 在类中定义__slots__变量来进行限定。
需要注意的是__slots__的限定值对当前对象生效，对子类并不起作用。
"""


class Person2(object):
    __slots__ = ("_name", "_age", "_gender")

    def __init__(self, name, age):
        self._name = name
        self._age = age

    @property
    def name(self):
        return self._name

    @property
    def age(self):
        return self._age

    @age.setter
    def age(self, age):
        self._age = age

    def play(self):
        if self._age <= 16:
            print("%s正在玩飞行棋." % self._name)
        else:
            print("%s正在斗地主." % self._name)


def main():
    person2 = Person2("BJZ", 22)
    person2.play()
    person2._gender = "男"
    # person2._isPlay = True


"""
静态方法和类方法
之前，我们在类中定义的方法都是对象方法，也就说这些方法都是发送给对象的消息，实际上，我们在类中并不需要都是对象方法，
例如我们定义一个三角形类，通过传入三角形长来构造三角形，并提供计计算周长和面积的方法
但是传入的三条边未必能够构造出三角形
因此我们可以险些一个方法来验证三角形边是是否可以构成三角形
这个方法很显然就不是对象方法，因为调用这个方法时三角形对象尚未创建出来(因为都不知道三条边能不能构建出三角形)
所以方法时西湖雨三角形类并不属于三角形对象的，我们可以使用静态对象来解决这类问题。
"""

from math import sqrt


class Triangle(object):

    def __init__(self, a, b, c):
        self._a = a
        self._b = b
        self._c = c

    @staticmethod
    def is_valid(a, b, c):
        # return a + b > c and b > c > a and a + c > b
        return a + b > c and a < c < b < a + c  # 简写

    def perimeter(self):
        return self._a + self._b + self._c

    def area(self):
        half = self.perimeter() / 2
        return sqrt(half * (half - self._a) * (half - self._b) * (half - self._c))


def triangleTest():
    a, b, c = 4, 4, 5

    if Triangle.is_valid(a, b, c):
        t = Triangle(a, b, c)
        print(t.perimeter())
        # 也可以通过给类发消息来调用方法但是要传入接受消息的对象作为参数
        print(Triangle.perimeter(t))
        print(t.area())
    else:
        print("无法构成三角形")


if __name__ == "__main__":
    triangleTest()

"""
和静态方法比较类似，Python也可以在类中定义类方法，类方法的第一个参数约定名为cls，它代表的是当前类相关的信息对象类本身也是一个对象，有的对象也称之为类的元数据对象)，通过这个参数我们可以获取和类相关的信息并且可以创建出类的对象
"""

from time import time, localtime, sleep


class Clock(object):
    """ 数字时钟 """

    def __init__(self, hour=0, minute=0, second=0):
        self._hour = hour
        self._minute = minute
        self._second = second

    @classmethod
    def now(cls):
        ctime = localtime(time())
        return cls(ctime.tm_hour, ctime.tm_min, ctime.tm_sec)

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


def main():
    # 通过类方法创建对象并获取系统时间
    clock = Clock.now()

    while True:
        print(clock.show())
        sleep(1)
        clock.run()


# if __name__ == "__main__":
#     main()

"""
类之间的关系
简单的来说，类和类之间的关系又三种：is-a、has-a和use-a的

    is-a关系也叫继承或者泛化，比如学生和人的关系，手机和电子产品的关系都属于继承关系
    has-a关系通常称之为关联，比如部门和员工的关系，骑车和引擎的关系，关联关系如果是整体和部分的关联，那么我们称之为聚合关系
    如果整体进一步负责了部分生命周期(整体的部分是不可分割的，同时同在也同时消亡)，那么这就是最强的关联关系，我们称之为合成关系。
    use-a关系通常称之为依赖，比如私有有一个驾驶的行为(方法)，其中(的参数)使用到了汽车，那么汽车和司机的关系就是依赖关系。
    
    
    利用类之间的关系，我们可以在已有类的基础上来完成某些操作，也可以在已有类的基础上创建新的类，这些都是实现代码服用的重要手段。
    服用现有的代码不经可以减少开发的工作量，也有利于代码的的关系和维护，这是我们在日常工作中都会使用到的技术手段。

"""

"""
继承和堕胎
在已有类的基础上创建新类，这其中的一种做法就是让一个类从另外一个类那里将属性和方法直接继承下来，从而减少重复代码的编写。
提供继承信息的我们称之为父类，也叫超类或者基类，得到继承 信息的我们称之为子类，也叫派生类或者衍生类
子类除了继承弗雷他提供的方法，还可以定义自己特有的属性和方法，所以子类比父类拥有更多能力，
在实际开发中，我们经常会用到子类对象去替换一个父类对象，这是面向对象编程中一个常见的行为，对应的原则称为：里氏替换原则。
"""


class Person3(object):
    """ 人 """

    def __init__(self, name, age):
        self._name = name
        self._age = age

    @property
    def name(self):
        return self._name

    @property
    def age(self):
        return self._age

    @age.setter
    def age(self, age):
        self._age = age

    def play(self):
        print("%s正在愉快的玩耍." % self._name)

    def watch_tv(self):
        if self._age >= 18:
            print("%s正在看CCTV." % self._name)
        else:
            print("%s只能看熊出没." % self._name)


class Student(Person3):
    """ 学生 """

    def __init__(self, name, age, grade):
        super().__init__(name, age)
        self._grade = grade

    @property
    def grade(self):
        return self._grade

    @grade.setter
    def grade(self, grade):
        self._grade = grade

    def study(self, course):
        print("%s的%s正在学习%s." % (self._grade, self._name, course))


class Teacher(Person3):
    """ 老师 """

    def __init__(self, name, age, title):
        super().__init__(name, age)
        self._title = title

    @property
    def title(self):
        return self._title

    @title.setter
    def title(self, value):
        self._title = value

    def teach(self, course):
        print("%s%s正在将%s." % (self._name, self._title, course))


def extentsTest():
    stu = Student("Andrew", 16, "初三")
    stu.study("数学")
    stu.watch_tv()

    tec = Teacher("BJZ", 32, "砖家")
    tec.teach("Python程序设计")
    tec.watch_tv()


if __name__ == "__main__":
    extentsTest()

"""
子类在继承父类的方法后，可以对父类以后的发给发给出新的实现版本，这个东躲称之为方法的重写(override)。通过方法重写我们可以让父类的
同一个行为在子类中拥有不同的实现版本，当我们调用这个就经过子类重写的方法时，不同的子类对象会表现出不同的行为，这个就是多态.
"""

from abc import ABCMeta, abstractmethod


class Pet(object, metaclass=ABCMeta):
    """ 宠物 """

    def __init__(self, nickname):
        self._nickname = nickname

    @abstractmethod
    def make_voice(self):
        """ 发出声音 """
        pass


class Dog(Pet):
    """ 狗 """

    def make_voice(self):
        print("%s: 汪汪汪..." % self._nickname)


class Cat(Pet):
    """ 猫 """

    def make_voice(self):
        print("%s: 喵喵喵..." % self._nickname)


def petTest():
    pets = [Dog("旺财"), Cat("凯迪"), Dog("大黄")]
    for pet in pets:
        pet.make_voice()


if __name__ == "__main__":
    petTest()

""" 我们将Pet类处理成了一个抽象类，所谓抽象类就是不能够创建兑现搞得类，这种类的存在就是专门为了让其他类去继承它
Python从语法层面没有像Java等语言那样提供对抽象类的支持，但是我们可以通过abc模块的ABCMeta元类和abstractmethod包装器来达到抽象类的效果。
如果一个类上面存在抽象方法那么这个类就不能被实例化。
上面代码中，Dog和Cat两个子类分别对Pet类中的make_voice方法进行了重写并给出了不同的实现版本，当我们在函数中调用该方法的时候
这个方法就表现出了堕胎的行为(同样的方法做了不同的事情)。
"""
