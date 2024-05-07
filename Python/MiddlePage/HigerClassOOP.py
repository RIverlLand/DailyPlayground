#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from types import MethodType

class Student(object):
    def __init__(self) -> None:
        pass

s = Student()
s.name = 'Bart'

print(s.name)

def set_age(self, age):
    self.age = age

s.set_age = MethodType(set_age, s)
s.set_age(25)
s.age == 25 # True

#! 给实例添加一个方法

s2 = Student()
s2.set_age(25) # returns error

# 注意只有一个实例添加了此方法

def set_score(self, score):
    self.score = score

Student.set_score = set_score

s3 = Student()
s3.set_score(60)
s3.score == 60 # True

#! 给实例添加属性是没问题的，只要不是修改private的属性

# 使用__slots__
# 但是，如果我们想要限制实例的属性怎么办？比如，只允许对Student实例添加name和age属性。

#! 为了达到限制的目的，Python允许在定义class的时候，定义一个特殊的__slots__变量，来限制该class实例能添加的属性：

class limitedStudent(object):
    __slots__ = ('name', 'age') # 用tuple定义允许绑定的属性名称

# 使用__slots__要注意，__slots__定义的属性仅对当前类实例起作用，对#!继承的子类是不起作用的：

class GraduateStudent(limitedStudent):
    pass

g = GraduateStudent()
g.score = 9999 # no error   除非在子类中也定义__slots__，这样，子类实例允许定义的属性就是自身的__slots__加上父类的__slots__

# 但在一个类之外随意更改其属性是一个不合理的行为，所以需要一些方法来限制对其属性的修改，例如：
class Student(object):

    def get_score(self):
         return self._score

    def set_score(self, value):
        if not isinstance(value, int):
            raise ValueError('score must be an integer!')
        if value < 0 or value > 100:
            raise ValueError('score must between 0 ~ 100!')
        self._score = value

# 但是，上面的调用方法又略显复杂，没有直接用属性这么直接简单。

# 有没有既能检查参数，又可以用类似属性这样简单的方式来访问类的变量呢？对于追求完美的Python程序员来说，这是必须要做到的！

# 还记得装饰器（decorator）可以给函数动态加上功能吗？对于类的方法，装饰器一样起作用。Python内置的@property装饰器就是负责把一个方法变成属性调用的

class Student(object):

    @property
    def score(self):
        return self._score

    @score.setter
    def score(self, value):
        if not isinstance(value, int):
            raise ValueError('score must be an integer!')
        if value < 0 or value > 100:
            raise ValueError('score must between 0 ~ 100!')
        self._score = value

# >>> s = Student()
# >>> s.score = 60 # OK，实际转化为s.set_score(60)
# >>> s.score # OK，实际转化为s.get_score()
# 60
# >>> s.score = 9999
# Traceback (most recent call last):
#   ...
# ValueError: score must between 0 ~ 100!
# 注意到这个神奇的@property，我们在对实例属性操作的时候，就知道该属性很可能不是直接暴露的，而是通过getter和setter方法来实现的。

# 还可以定义只读属性，只定义getter方法，不定义setter方法就是一个只读属性： #! getter 和 setter本身应该不是装饰器或者property的默认方法，只是一个叫法，似乎是从java来的
class Student(object):

    @property
    def birth(self):
        return self._birth

    @birth.setter
    def birth(self, value):
        self._birth = value

    @property
    def age(self):
        return 2015 - self._birth
    
# 要特别注意：属性的方法名不要和实例变量重名。例如，以下的代码是错误的：

class Student(object):

    # 方法名称和实例变量均为birth:
    @property
    def birth(self):
        return self.birth
#! 这是因为调用s.birth时，首先转换为方法调用，在执行return self.birth时，又视为访问self的属性，于是又转换为方法调用，造成无限递归，最终导致栈溢出报错RecursionError。



# 请利用@property给一个Screen对象加上width和height属性，以及一个只读属性resolution：:
class Screen(object):
    @property
    def width(self):
        return self._width
    @width.setter
    def width(self, width):
        self._width = width
    @property
    def height(self):
        return self._height
    @width.setter
    def height(self, height):
        self._height = height
    @property
    def resolution(self):
        return self._height * self._width