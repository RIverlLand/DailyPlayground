#!/usr/bin/env python3
# -*- coding: utf-8 -*-

class Student(object):
    def __init__(self) -> None:
        pass

s = Student()
s.name = 'Bart'

print(s.name)

def set_age(self, age):
    self.age = age

from types import MethodType

s.set_age = MethodType(set_age, s)
s.set_age(25)
s.age == 25 # True

s2 = Student()
s2.set_age(25) # returns error

def set_score(self, score):
    self.score = score

Student.set_score = set_score

s3 = Student()
s3.set_score(60)
s3.score == 60 # True

# 使用__slots__
# 但是，如果我们想要限制实例的属性怎么办？比如，只允许对Student实例添加name和age属性。

#! 为了达到限制的目的，Python允许在定义class的时候，定义一个特殊的__slots__变量，来限制该class实例能添加的属性：

class limitedStudent(object):
    __slots__ = ('name', 'age') # 用tuple定义允许绑定的属性名称

# 使用__slots__要注意，__slots__定义的属性仅对当前类实例起作用，对#!继承的子类是不起作用的：

class GraduateStudent(limitedStudent):
    pass

g = GraduateStudent()
g.score = 9999 # no error