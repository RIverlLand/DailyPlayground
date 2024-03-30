# OOP把对象作为程序的基本单元，一个对象包含了数据和操作数据的函数。

# 面向过程的程序设计把计算机程序视为一系列的命令集合，即一组函数的顺序执行。为了简化程序设计，面向过程把函数继续切分为子函数，即把大块函数通过切割成小块函数来降低系统的复杂度。

# 而面向对象的程序设计把计算机程序视为一组对象的集合，而每个对象都可以接收其他对象发过来的消息，并处理这些消息，计算机程序的执行就是一系列消息在各个对象之间传递。

# 如果要打印一个学生的成绩，首先必须创建出这个学生对应的对象，然后，#! 给对象发一个print_score消息，让对象自己把自己的数据打印出来。

class Student(object):

    def __init__(self, name, score):  # __init__方法的第一个参数永远是self，表示创建的实例本身，因此，在__init__方法内部，就可以把各种属性绑定到self，#! 因为self就指向创建的实例本身。
        self.name = name
        self.score = score

    def print_score(self):
        print('%s: %s' % (self.name, self.score))
# 给对象发消息实际上就是调用对象对应的关联函数，我们称之为对象的方法 #!（Method）
        
# 类（Class）和实例（Instance）的概念是很自然的。Class是一种抽象概念，比如我们定义的Class——Student，是指学生这个概念，而实例（Instance）则是一个个具体的Student
        
# 也就是说，Instance来自同一个类，有着相同的方法，但是各自的数据完全不同
        
bart = Student() # 创建一个instance是通过类名+()实现的 但当类本身具有__init__ 方法的时候，传入就不可以为空，而是要将init需要的参数写入
bart = Student('bart', 80)

# 由于self指向的是实例本身，print_score函数中的self也就指向了bart，所以可以直接调用来打印该instance的数据

# 和静态语言不同，#! Python允许对实例变量绑定任何数据，
# 也就是说，对于两个实例变量，虽然它们都是同一个类的不同实例，但拥有的变量名称都可能不同：

# Appendix:

# 动态语言（弱类型语言）是运行时才确定数据类型的语言，变量在使用之前无需申明类型，通常变量的值是被赋值的那个值的类型。比如Php、Asp、JavaScript、Python、Perl等等。
# var s ="hello";
# var i = 0;
# var b = true;
# 静态语言（强类型语言）是编译时变量的数据类型就可以确定的语言，大多数静态语言要求在使用变量之前必须生命数据类型。比如Java、C、C++、C#等。
# String s="hello";    //String 类型的变量
# boolean b=true;    //boolean 类型的变量
# int i=0;    //int 类型的变量