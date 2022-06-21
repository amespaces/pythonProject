# 对于可迭代对象， 可以使用next函数去获取元素如果获取完了会抛出StopIteration提示
alist = [0, 1, 2]
gen = iter(alist)
listnum1 = next(gen)
print(listnum1)
# 对于可迭代对象，迭代器内部只是多了一个函数__next__()
# 要创建可迭代器，需要创建一个可迭代对象
from collections.abc import Iterator


class Array:
    index = 0
    mylist = [0, 1, 2]

    def __iter__(self):
        return self

    def __next__(self):
        if self.index <= len(self.mylist) - 1:
            value = self.mylist[self.index]
            self.index += 1
            return value
        raise StopIteration
