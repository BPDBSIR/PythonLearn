"""
列表(list)和元组(tuple)

List: 是一种有序的集合，可以随时添加和删除其中的元素

比如，列出班里所有女同学的名字，就可以使用一个list表示：
"""
classmates = ['Michael', 'Bob', 'Tracy']

print(classmates)

# 变量classmates就是一个list。用len()函数可以获得list元素的个数：
print(len(classmates))

# 用索引来访问list中每一个位置的元素，记得索引是从0开始的

print(classmates[0])

print(classmates[1])

print(classmates[2])

# print(classmates[3])  # 索引越界抛出异常

# 当索引超出了范围时，Python会报一个IndexError错误，所以，要确保索引不要越界，记得最后一个元素的索引是len(classmates) - 1。

# 如果要取最后一个元素，除了计算索引位置外，还可以用-1做索引，直接获取最后一个元素
print(classmates[-1])

# 以此类推，可以获取倒数第2个、倒数第3个：
print(classmates[-2])

print(classmates[-3])

# list是一个可变的有序表，所以，可以往list中追加元素到末尾：
classmates.append("Andrew")

print(classmates)

# 也可以把元素插入到指定的位置，比如索引号为1的位置
classmates.insert(1, "James")  # 原来索引为1的元素就向后移 则为2
print(classmates)

# 要删除list末尾的元素，使用pop()方法
classmates.pop()
print(classmates)

# 要删除指定位置的元素，使用pop(index)方法，index为索引
classmates.pop(1)
print(classmates)

# 要把搜个元素替换成别的元素，可以在hi姐赋值给对应的索引位置
classmates[1] = "Andrew"
print(classmates)

# List里面的元素的数据类型也可以不相同
arr = ["Apple", 123, True]
print(arr)

# list元素也可以是另外一个list
s = ["Python", "Java", ["Kotlin", "Swift"], "Jetpack Compose"]
print(len(s))
print(s)

# 此时可以将s看成一个二维数组，则可以这样读取数据
print(s[2][0])

# 如果一个list中一个元素也没有，就是一个空的list，它的长度为0
emptyList = []
print(emptyList)
print(len(emptyList))

"""
tuple
另一种有序列表叫做元组：tuple，他与list非常类似
但是tuple一旦初始化就不能修改，比如同样是列出同学的名字
"""
classmates = ("Andrew", "BPDBSIR", "James")
print(classmates)

# 现在classmates的内容不能改变了，它没有apple、insert这样的方法，其他获取元素的方和和list是一样的
# 你可以正常使用classmates[0]、classmates[-1]这样的方法，但是不能赋值为另外的元素

# 不可变的tuple有什么意义呢？因为tuple不可变，所以代码更安全，如果可能，能使用tuple代替list就尽量使用tuple

# tuple的陷阱：当你定义一个tuple时，在定义的时候，tuple的元素就必须被定下来
t = (1, 2)
print(t)

# 如果要定义一个空的tuple，可以直接写成()
t = ()
print(t)

# 但是，要定义一个只有一个元素的tuple，如果你这么定义
t = (1)
print(t)  # 1 输出的结果是1
# 定于一的就不是tuple，是1这个数字，这是因为括号()既可以表示tuple，又可以表示数学公式中的小括号
# 这就产生了歧义，因此，在这种情况下，按小括号进行计算，计算结果自然是1 所以，只有一个元素的tuple定义时，必须加上一个, 来消除歧义
t = (1,)
print(t)
# Python在显示只有1个元素的tuple时，也会加一个逗号,，以免你误解成数学计算意义上的括号。


# 最后来看一个“可变的”tuple：
t = ('A', 'B', ['c', 'd'])
t[2][0] = "X"
t[2][1] = "Y"
print(t)

# 实际上，这里索引为2的元素是一个list，我们不能修改tuple但是可以修改list



