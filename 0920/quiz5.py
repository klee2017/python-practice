def mymax(*args):
    result = args[0]
    try:
        for i in args:
    #list 이기 때문에 바로 입력 가능
            if result < i:
                result = i
        return result
    except:
        print('Invalid arguments')

print(mymax(2, 45, 3, 6, 2, 30, 38, 53, 9))
