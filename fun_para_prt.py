def product(*n):
	if(len(n)) <= 0:
		raise TypeError('At least one parameter is wanted!')
	s = 1
	for i in n:
		if not isinstance(i,(int,float)):
			raise TypeError('Wrong Number!')
		s = s * i
	return s
