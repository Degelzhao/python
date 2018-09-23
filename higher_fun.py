#map(),reduce()
#利用map()函数，把用户输入的不规范的英文名字，变为首字母大写，其他小写的规范名字
def normaliza(name):
	name = name[0].upper() + name[1:].lower()
	return name

L1 = ['adam', 'LISA', 'barT']
L2 = list(map(normaliza,L1))
print(L2)

#filter()
#回数是指从左向右读和从右向左读都是一样的数，例如12321，909。请利用filter()筛选出回数：
#str(n)[::-1]:表示一个切片，从列表最后一位开始，步长为-1，即从[-1]开始，索引值每次累加-1
def is_palindrome(n):
	return str(n) == str(n)[::-1]

output = filter(is_palindrome,range(1,10000))
print(list(output))

#sorted()
#1.假设我们用一组tuple表示学生名字和成绩：
#L = [('Bob', 75), ('Adam', 92), ('Bart', 66), ('Lisa', 88)]
#请用sorted()对上述列表按名字升序排序：
def by_name(t):
	return t[0]
L = [('Bob', 75), ('Adam', 92), ('Bart', 66), ('Lisa', 88)]
L1 = sorted(L,key = by_name)
print(L1)

#请用sorted()对上述列表按成绩降序	排序：
def by_scort(t):
	return t[1]
L = [('Bob', 75), ('Adam', 92), ('Bart', 66), ('Lisa', 88)]
L1 = sorted(L,key = by_scort,reverse = True)
print(L1)