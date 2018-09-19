L1 = ['Hello', 'World', 18, 'Apple', None]
L = [s.lower() for s in L1 if isinstance(s,str)]
print(L)

L = [s.lower() if isinstance(s,str) else s for s in L1]
print(L)