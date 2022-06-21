# 可迭代对象：可以利用for循环的对象
from collections.abc import Iterable

# 列表、字典、元组、字符串 都是可迭代对象
list1 = [1, 2, 3]
# 如果使用__getitem__()方法获取元素，此时isinstance是无法判断是否是一个可迭代对象
res = isinstance(list1, Iterable)
print(res)


# 可迭代协议 如果一个类内部实现了__iter__() 方法并番薯一个迭代器实例就是可迭代对象
class Array:
    mylist = [0, 1, 2]

    def __iter__(self):
        return iter(self.mylist)


mylist = Array()
res1 = isinstance(mylist, Iterable)
print(res1)

