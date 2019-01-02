# any():用于判断给定的可迭代参数iterable是否全部为False，则返回False，如果有一个为True，则返回True
# 元素除了是0、空、False外都算TRUE

# all():用于判断给定的可迭代参数 iterable 中的所有元素是否都为 TRUE，如果是返回 True，否则返回 False。
# 元素除了是 0、空、FALSE 外都算 TRUE

x = [True, True, False]

if any(x):
    print("At least one True")

if all(x):
    print("Not one False")

if any(x) and not all(x):
    print("At least one True and one False")