animals = ('dog','bird','pig')
print(animals)
print(animals[0])
print(animals[-1])
print(animals[-2])

#define a tuple contain one element
god = ('me',)
print(god)

#you must know the tuple element is not change means the 
#position of every element is not change
#For example:
t = ('a','b',['A','B'])
print(t)
t[2][0] = 'X'
t[2][1] = 'Y'
print(t) 