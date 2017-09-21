def myfunc(*args):
    length = len(args)
    if length == 1:
        return args[0]**2
    elif length == 2:
        return args[0]*args[1]
    else:
        print('Invalid arguments')

print(myfunc(10))
