# 生成器不是列表，是iterable的object，和列表类似但不占内存，只有在被调用时计算其内容

# generator保存的是算法，每次调用next(g)，就计算出g的下一个元素的值，直到计算到最后一个元素，没有更多的元素时，抛出StopIteration的错误。

# 斐波那契

def fib(max):
    n, a, b = 0, 0, 1
    while n < max:
        print(b)
        a, b = b, a + b  #! ??
        # 其实是等式两边 a 和 b 分别 = b 和 a+b
        n = n + 1
    return 'done'

# a, b = b, a + b
# 相当于：
# t = (b, a + b) # t是一个tuple
# a = t[0]
# b = t[1]


# 此时的Fibonachi函数很接近一个generator，为了使他真正成为一个不占内存的好公民，可以把print改成yield:
# 如果一个函数定义中包含yield关键字，那么这个函数就不再是一个普通函数，而是一个generator函数，调用一个generator函数将返回一个generator：

def fib(max):
    n, a, b = 0, 0, 1
    while n < max:
        yield(b)
        a, b = b, a + b
        n = n + 1
    return 'done'
# 普通函数是顺序执行，遇到return语句或者最后一行函数语句就返回。而变成generator的函数，在每次调用next()的时候执行，遇到yield语句返回，再次执行时从上次返回的yield语句处继续执行。

# ---

def odd():
    print('step 1')
    yield 1
    print('step 2')
    yield(3)
    print('step 3')
    yield(5)

# output:
# >>> o = odd()
# >>> next(o)
# step 1
# 1
# >>> next(o)
# step 2
# 3
# >>> next(o)
# step 3
# 5
# >>> next(o)
# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
# StopIteration
# 调用generator函数会创建一个generator对象，多次调用generator函数会创建多个相互独立的generator。
    
    # 如果递归的调用odd()，则：
    
# >>> next(odd())
# step 1
# 1
# >>> next(odd())
# step 1
# 1
# >>> next(odd())
# step 1
# 1
    

# --- 杨辉三角
    # GPT
def YangTri(): # 没有Max值需要定义，杨辉三角本身不依托外部数值存在
    L = [1]
    while True:
        yield L
        L = [1] + [L[i] + L[i + 1] for i in range(len(L) - 1)] + [1]

# 定义杨辉三角的时候要考虑的是下一层（由当前层得来），所以yield在L的计算之前。调用generator之后L的数值其实是下一层的数值，但由于yield在前，返回的数值是当前层的。这也是为什么第一层需要提前定义
# 比较困难的是理解这个思路，以及这种做法等于每层都要运算一遍整个三角之前的所有层数？因为生成器并不会在地址中写入L[i]的数值，这就导致L[i+1]重新进行一边计算，也就是递归的复杂度？
        
