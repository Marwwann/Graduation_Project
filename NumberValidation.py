def NumberValidation(x):
    flag = 0
    try:
        float(x)
        flag = 1
    except ValueError:
        flag = 0

    if flag == 1:
        return True
    else:
        return False

x = 'r'
print(NumberValidation(x))
