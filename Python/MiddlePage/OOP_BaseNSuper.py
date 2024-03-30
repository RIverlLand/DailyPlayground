class Animal(object):
    def run(self):
        print('Animal is running...')

class Dog(Animal):
    pass


dog = Dog()
dog.run()


class Cat(Animal):
    def run(self):
        print('Cat is running...')

    def eat(self):
        print('Eating meat...')

# 子类和父类都存在相同的run()方法时，我们说，子类的run()覆盖了父类的run()，在代码运行的时候，总是会调用子类的run()。这样，我们就获得了继承的另一个好处：多态。
        
    # 判断一个变量是否是某个类型可以用isinstance()判断：
    # 所以 isinstane(8, int)， 代表着int是一个大类
        
# 当调用一个instance的时候，可以写作：
def run_twice(animal):
    animal.run()
    animal.run()

cat = Cat()
run_twice(cat) # Cat is running... /n Cat is running...

# 这就是多态真正的威力：调用方只管调用，不管细节，而当我们新增一种Animal的子类时，只要确保run()方法编写正确，不用管原来的代码是如何调用的。这就是著名的“开闭”原则：

# 对扩展开放：允许新增Animal子类；

# 对修改封闭：不需要修改依赖Animal类型的run_twice()等函数。




# 对于静态语言（例如Java）来说，如果需要传入Animal类型，则传入的对象必须是Animal类型或者它的子类，否则，将无法调用run()方法。

# 对于Python这样的动态语言来说，则不一定需要传入Animal类型。我们只需要保证传入的对象有一个run()方法就可以了：

class Timer(object):
    def run(self):
        print('Start...')
# 这就是动态语言的“鸭子类型”，它并不要求严格的继承体系，一个对象只要“看起来像鸭子，走起路来像鸭子”，那它就可以被看做是鸭子。
        

# isinstance还可以判断一个变量是否是某些类型中的一种，比如下面的代码就可以判断是否是list或者tuple：
# >>> isinstance([1, 2, 3], (list, tuple))
# True
# >>> isinstance((1, 2, 3), (list, tuple))
# True
        
# 如果要获得一个对象的所有属性和方法，可以使用dir()函数，它返回一个包含字符串的list，比如，获得一个str对象的所有属性和方法：

# >>> dir('ABC')
# ['__add__', '__class__',..., '__subclasshook__', 'capitalize', 'casefold',..., 'zfill']
        
# 一些双下划线的属性和方法都是特殊用途的python内容，例如在len()函数内部，它自动去调用该对象的__len__()方法，所以，下面的代码是等价的：

# >>> len('ABC')
# 3
# >>> 'ABC'.__len__()
# 3
        
#! 仅仅把属性和方法列出来是不够的，配合getattr()、setattr()以及hasattr()，我们可以直接操作一个对象的状态：

# >>> class MyObject(object):
# ...     def __init__(self):
# ...         self.x = 9
# ...     def power(self):
# ...         return self.x * self.x
# ...
# >>> obj = MyObject()
# 紧接着，可以测试该对象的属性：

# >>> hasattr(obj, 'x') # 有属性'x'吗？
# True
# >>> obj.x
# 9
# >>> hasattr(obj, 'y') # 有属性'y'吗？
# False
# >>> setattr(obj, 'y', 19) # 设置一个属性'y'
# >>> hasattr(obj, 'y') # 有属性'y'吗？
# True
# >>> getattr(obj, 'y') # 获取属性'y'
# 19
# >>> obj.y # 获取属性'y'
# 19
# 如果试图获取不存在的属性，会抛出AttributeError的错误：

# >>> getattr(obj, 'z') # 获取属性'z'
# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
# AttributeError: 'MyObject' object has no attribute 'z'
# 可以传入一个default参数，如果属性不存在，就返回默认值：

# >>> getattr(obj, 'z', 404) # 获取属性'z'，如果不存在，返回默认值404
# 404