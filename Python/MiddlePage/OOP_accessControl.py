class Student(object):

    def __init__(self, name, score):  #! self就指向创建的实例本身。
        self.name = name
        self.score = score

    def print_score(self):
        print('%s: %s' % (self.name, self.score))

# Student 类之中的参数可以随意的被外部函数修改，为了让其无法被外部直接访问和修改，可以将参数本身设为private

class StudentPri(object):

    def __init__(self, name, score):
        self.__name = name
        self.__score = score

    def print_score(self):
        print('%s: %s' % (self.__name, self.__score))

# 此时直接从外部调用将无法修改name score的内容。如果想要从外部访问数据而不是直接打印，则需要一些方法
    def get_name(self):
        return self.__name

    def get_score(self):
        return self.__score
    
# 如果又要允许外部代码修改score怎么办？可以再给Student类增加set_score方法：

    def set_score(self, score):
        self.__score = score

#! 参考得知为什么PythonAPI中的参数都是Get Set开头的，全部都是private变量
        
    # 需要注意的是，在Python中，变量名类似__xxx__的，也就是 **以双下划线开头，并且以双下划线结尾的** ，是特殊变量，特殊变量是可以直接访问的，不是private变量，所以，不能用__name__、__score__这样的变量名。
        
# 有些时候，你会看到以一个下划线开头的实例变量名，比如_name，这样的实例变量外部是可以访问的，但是，按照约定俗成的规定，当你看到这样的变量时，意思就是，“虽然我可以被访问，但是，请把我视为私有变量，不要随意访问”。

#! 双下划线开头的实例变量是不是一定不能从外部访问呢？其实也不是。不能直接访问__name是因为Python解释器对外把__name变量改成了_Student__name，所以，仍然可以通过_Student__name来访问__name变量：

# >>> bart._Student__name
# 'Bart Simpson'
# 不同版本的Python解释器可能会把__name改成不同的变量名。
        

# 但总结来说，python并没有任何的机制来保护private的参数或函数，全靠自觉
        


# 最后注意下面的这种 #!错误写法：

# >>> bart = Student('Bart Simpson', 59)
# >>> bart.get_name()
# 'Bart Simpson'
# >>> bart.__name = 'New Name' # 设置__name变量！
# >>> bart.__name
# 'New Name'
# 表面上看，外部代码“成功”地设置了__name变量，但实际上这个__name变量和class内部的__name变量不是一个变量！内部的__name变量已经被Python解释器自动改成了_Student__name，而外部代码给bart新增了一个__name变量。不信试试：

# >>> bart.get_name() # get_name()内部返回self.__name
# 'Bart Simpson'
        
        # practice:请把下面的Student对象的gender字段对外隐藏起来，用get_gender()和set_gender()代替，并检查参数有效性
        
class Student(Object):
    def __init__(self, name, gender):
        self.name = name
        self.__gender__ = gender
    
    def get_gender(self):
        return self.__gender__

    def set_gender(self, setgender):
        if setgender == 'male' or 'female':
            self.__gender__ = setgender
        else:
            Warning('wrong input')