#杨辉三角
def triangles(max):
	p = [1]
	while True:
		yield p
		p = [1] + [p[i] + p[i+1] for i in range(len(p) -1)] + [1]
		
