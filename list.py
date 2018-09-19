classments = ['Barry','Lucy','Bob','Sunny']
print(classments)
print(classments[3])
print(classments[-1])
print(classments[-2])
print(classments[-3])
print(classments[-4])

#append a new element#
classments.append('s4')
print(classments[-1])

#add a new element to designated position
classments.insert(0,'Jack')
print(classments[0])

#delete the end of element
classments.pop()
print(classments)

#delete the designated position element
classments.pop(0)
print(classments)

#replace the value of the element
classments[0] = 'sarah'
print(classments)

age = [20,21,22,classments,23]
print(age)
print(age[-2])
print(age[3][2])