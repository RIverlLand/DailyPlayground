# 列表生成器的 if else语句用法

# 合规的两个
[x for x in range(1, 11) if x % 2 == 0]

[x if x % 2 == 0 else -x for x in range(1, 11)]

# 跟在for后面的if是一个筛选条件，不能带else
# 但else 后跟pass continue 是非法的

# [points[i] for i in len(points)] 是非法的，生成器中不可以调用index调用

# *var 可变参数，传入的参数需要是一个tuple 或者 list

def calc(*numbers):
    sum = 0
    for n in numbers:
        sum = sum + n * n
    return sum

# **kw 关键字参数，可以传入0或者多个参数

def person(name, age, **kw):
    print('name:', name, 'age:', age, 'other:', kw)

# str(n)[::-1] # [::-1]代表倒序的从尾到头组成list