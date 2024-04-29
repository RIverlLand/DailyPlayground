import copy

class Person:
    def __init__(self, name, friends=None):
        self.name = name
        if friends is None:
            self.friends = []
        else:
            self.friends = friends

    def __repr__(self):
        return f"Person(name={self.name}, friends={self.friends})"

# 创建一个原始 Person 对象
alice = Person("Alice", ["Bob", "Charlie"])

# 对 alice 进行浅拷贝
shallow_copy_alice = copy.copy(alice)

# 修改浅拷贝对象的 friends 列表
shallow_copy_alice.friends.append("David")

print("原始对象：", alice)  # 原始对象的 friends 列表也被修改了
print("浅拷贝对象：", shallow_copy_alice)

# 对 alice 进行深拷贝
deep_copy_alice = copy.deepcopy(alice)

# 修改深拷贝对象的 friends 列表
deep_copy_alice.friends.append("David")

print("原始对象：", alice)  # 原始对象的 friends 列表保持不变
print("深拷贝对象：", deep_copy_alice)