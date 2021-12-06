def CheckInput(x):
    a = x.split(':')
    CheckList = []
    OriginalList = []
    for i in range(len(a)):
        OriginalList.append('T')
        try:
            w = float(a[i])
            if isinstance(w, float):
                CheckList.append('T')
        except ValueError:
            CheckList.append('F')

        '''
        if a[i].isdigit():
            CheckList.append('T')
        else:
            CheckList.append('F')
    print(CheckList)
    print(OriginalList)
    if CheckList == OriginalList:
        return True
    else:
        return False
'''
    if CheckList == OriginalList:
        return True
    else:
        return False
#q = '0.1::1'
#print(CheckInput(q))