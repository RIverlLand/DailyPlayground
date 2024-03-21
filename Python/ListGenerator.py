# 列表生成器的 if else语句用法

# 合规的两个
[x for x in range(1, 11) if x % 2 == 0]

[x if x % 2 == 0 else -x for x in range(1, 11)]

# 跟在for后面的if是一个筛选条件，不能带else
# 但else 后跟pass continue 是非法的