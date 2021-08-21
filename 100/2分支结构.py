"""
分支结构
迄今为止，我们辨析的代码都是一条一条语句执行的，这种代码结构通常成为顺序结构，然而顺序结构并不能解决u所有的问题
比如我们设计一个游戏，游戏的第一关的通关雕件的玩家通过1000分，那么在完成本剧游戏后，我们要根据玩家得到的分数来决定是否进入第二关
还是告诉玩家GameOver，这里就会产生两个分支，而且这两个分支只有一个会被执行
类似的场景还有很多我们将这种结构称之为分支结构或者选择结构
"""

"""
if语句的使用
要构造分支结构可以使用if、elif和else关键字，所谓挂念子就是有特殊含义的单词，想if和else就是专门用于构造分支结构的关键字
很显然你不能使用它作为变量
"""
username = input("请输入用户名: ")
password = input("请输入密码: ")
if username == "admin" and password == "123456":
    print("身份验证成功")
else:
    print("身份验证失败")

"""
和Java等语言不同，Python中没有使用花括号来构造代码块而是使用了缩进的方式来标识代码的层次结构，如果if条件成立的情况下需要执行多条语句
只需要报纸多条语句具有相同的缩进就可以了
建议不要使用指标见或者设置你的代码编辑工具自动将制表建变成4个空格

当然徐国要构造更多的分支可以使用if...elif...else...结构或者嵌套的if...else结构
"""
x = float(input("x = "))
if x > 1:
    y = 3 * x - 5
elif x >= -1:
    y = x + 2
else:
    y = 5 * x + 3
print("f(%.2f) = %.2f" % (x, y))

""" 当然根据实际开发的需要，分支结构是可以嵌套的 """

x = float(input('x = '))
if x > 1:
    y = 3 * x - 5
else:
    if x >= -1:
        y = x + 2
    else:
        y = 5 * x + 3
print('f(%.2f) = %.2f' % (x, y))

"""
在之前我们提到的Python之禅中有这么一句话“Flat is better than nested.”
之所以提倡代码“扁平化”是因为嵌套结构的嵌套层次多了之后会严重的影响代码的可读性，所以能使用扁平化的结构时就不要使用嵌套。
"""

"""
英制的那位英寸与公制单位厘米互换
"""
value = float(input("请输入长度："))
unit = input("请输入单位：")
if unit == "in" or unit == "英寸":
    print("%f英寸 = %f厘米" % (value, value * 2.54))
elif unit == "cm" or unit == "厘米":
    print("%f厘米 = %f英寸" % (value, value / 2.54))
else:
    print("请输入有效的单位")

"""
百分之成绩转换为等级制成绩
要求：
如果输入的成绩在
    90分 以上(含90分) 输出A
    80-90分(不含90分) 输出B
    70-80分(不含80分) 输出C
    60-70分(不含70分) 输出D
    60分以下输出E
"""
score = float(input("请输入成绩："))
if score >= 90:
    grade = 'A'
elif score >= 80:
    grade = 'B'
elif score >= 70:
    grade = 'C'
else:
    grade = 'D'
print("对应的等级是: ", grade)

"""
输入三条边长，如果能构成三角形就计算周长和面积
"""
a = float(input("第一条边："))
b = float(input("第二条边："))
c = float(input("第三条边："))
if a + b > c and a + c > b and b + c > a:
    print("周长: %f" % (a + b + c))
    p = (a + b + c) / 2
    area = (p * (p - a) * (p - b) * (p - c)) ** 0.5
    print('面积: %f' % area)
else:
    print("不能构成三角形")
