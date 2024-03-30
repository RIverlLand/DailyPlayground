from functools import partial
 
def mod(x, y=2):  # 判断是否是偶数
    return x % y == 0

mod3 = partial(mod, y=3) # 判断是否是3的倍数

print(mod(4))
print(mod3(9))
# 两个输出都是True
