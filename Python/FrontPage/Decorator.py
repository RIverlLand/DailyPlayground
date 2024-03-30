# 装饰器：这种在代码运行期间动态增加功能的方式
def log(func):
    def wrapper(*args, **kw): 
        print("call %s()" % func.__name__)
        return func(*args, **kw)
    return wrapper

@ log
def now(a):
    print('2024.03.28 by %s' % a)

# 此时相当于调用了log(now)
now('yehan') #! 如果在这一行pause, now.__name__ 会变成wrapper，而不是now

# 如果decorator本身需要一些参数传入，则需要多写一层进行包装