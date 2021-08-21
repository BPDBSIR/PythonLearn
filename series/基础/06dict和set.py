"""
dict
Python内置了字典：dict的支持，dict全称dictionary，在其他语言中也称为map，使用键-值（key-value）存储，具有极快的查找速度。

举个例子，假设要根据同学的名字查找对应的成绩，如果用list实现，需要两个list：

给定一个名字，要查找对应的成绩，就先要在names中找到对应的位置，再从scores取出对应的成绩，list越长，耗时越长。
如果用dict实现，只需要一个“名字”-“成绩”的对照表，直接根据名字查找成绩，无论这个表有多大，查找速度都不会变慢。用Python写一个dict如下：
"""

maps = {
    "Andrew": 100,
    "BPDBSIR": 98,
    "James": 88
}
print(maps["Andrew"])

"""
为什么dict查找速度这么快？因为dict的实现原理和查字典是一样的。
假设字典包含了1万个汉字，我们要查某一个字 一个办法是把字典从第一页往后翻，直到找到我们想要的字为止  这种方法就是在list中查找元素的方法，list越大，查找越慢。

第二种方法是先在字典的索引表里（比如部首表）查这个字对应的页码 ，然后直接翻到该页，找到这个字。无论找哪个字，这种查找速度都非常快，不会随着字典大小的增加而变慢。

dict就是第二种实现方式，给你一个名字，比如Andrew，dict内部就可以直接计算出Andrew对应存放成绩的页码，也就是100这个数字存放的内存地址，直接取出来，所以速度非常快。

"""

# 你可以猜到这种key-value的储存方式，在放过进去的时候，必须根据key算出value的存放位置，这样我们取的时候才能根据key直接拿到value

# 把数据放入dict的方法，除了初始化时指定外，还可以通过key放入：
maps["BJZ"] = 200
print(maps["BJZ"])

# 由于一个key只能对应一个value，所以，多次对一个key放入value，后面的值会把前面的值冲掉：
maps["Andrew"] = 59
print(maps["Andrew"])

# 如果key不存在，dict就会报错：
# print(maps["Tom"])

# 要避免key不存在的错误，有两种办法，一是通过in判断key是否存在：
print("Tom" in maps)

# 二是通过dict提供的get()方法，如果key不存在，可以返回None，或者自己指定的value：
print(maps.get("Tom"))
print(maps.get("Tom", 66))

# 注意：返回None的时候Python的交互环境不显示结果。

# 要删除一个key，用pop(key)方法，对应的value也会从dict中删除：
print(maps.pop("BPDBSIR"))
# print(map["BPDBSIR"])

# 请务必注意，dict内部存放的顺序和key放入的顺序是没有关系的。

"""
和list比较，dict有以下几个优点: 
查找和插入的速度很快，不会随着key的增加而变慢
需要占用的阿亮的内存，内存浪费多

而list相反
查找和插入的时间随着元素的增加而增加
占用空间小，浪费内存很少
"""

# dict可以用在需要高速查找的很多地方，在Python代码中几乎无处不在，正确使用dict非常重要，需要牢记的第一条就是dict的key必须是不可变对象。

# 这是因为dict根据key来计算value的存储位置，如果每次计算相同的key得出的结果不同，那dict内部就完全混乱了。这个通过key计算位置的算法称为哈希算法（Hash）。

# 要保证hash的正确性，作为key的对象就不能变。在Python中，字符串、整数等都是不可变的，因此，可以放心地作为key。而list是可变的，就不能作为key


"""
set
set和dict雷士，也是一组key的集合，单不储存value，由于key不能重复，所以在set中，没有重复的key 
"""

# 要创建一个set，需要提供一个list作为输入集合：
s = set([1, 2, 3])
print(s)

# 注意传入的参数[1,2,3]是一个list，而显示的{1,2,3}是 告诉你这个set内部有1,2,3这三个元素，显示的顺序不表示set是有序的


# 重复元素在set中自动被过滤：
s = set([1, 1, 2, 2, 3, 3])
print(s)

# 通过add(key)方法可以添加元素到set中，可以重复添加，但不会有效果：
s.add(4)
print(s)
s.add(9)
print(s)

# 通过remove(key)方法可以删除元素：
s.remove(4)
print(s)

# set可以看成数学意义上的无序和无重复元素的集合，因此，两个set可以做数学意义上的交集、并集等操作：
s1 = set([1, 2, 3])
s2 = set([2, 3, 4])
print(s1 & s2)
print(s1 | s2)

# set和dict的区别在于没有储存对应的value，但是set的原理和dict一样，所以同样不可以放入可变对象，因为无法判断两个可变的对象是否相等
# 也就无法保存set内部不会有重复元素，试试把list放入set看看是否会报错


"""
再以不可变对象
str是不可变对象，而list是可变对象
"""
# 对于可变对象，比如list，而list进行 操作，list内部的内容是会变化的：
a = ["C", "B", "A"]
a.sort()
print(a)

# 而对于不可变对象，比如str：
a = "abc"
b = a.replace("a", "A")
print(a)
print(b)

# 虽然字符串有个replace方法，也确实变出了Abc，到那时变量a最后仍然是abc

# 要牢记的是，a是变量，而"abc"才是字符串本身，有些时候，我们经常说，对象a的内容是abc，但其实是值，a本身是一个变量，它指向的对象的内容才是abc

# 当我们调用a.replace('a','A')时，实际上调用方法replace是作用在字符串对象abc上的，而这个方法虽然叫replace
# 但却没有改变abc的内容，箱单replace方法创建了一个新的字符串Abc并返回，如果我们用变量b重新指向了该字符串，就容易理解了
# 变量a仍然指向原有的字符串abc，但变量b却指向了新的字符串Abc了

# 所以，对于不变对象来说，调用对象自身的任意方法，也不会改变该对象自身的内容。相反，这些方法会创建新的对象并返回，这样，就保证了不可变对象本身永远是不可变的。

# 使用key-value存储结构的dict在Python中非常有用，选择不可变对象作为key很重要，最常用的key是字符串。

