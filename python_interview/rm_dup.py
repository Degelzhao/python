def dellist(L):
    L1 = []
    for i in L:
        if i not in L1:
            L1.append(i)

    return L1

if __name__ == '__main__':
    print(dellist([1,2,3,2,4,3,5]))