def mydecorator(f):
    def ret_func(*args):
        print(len(args), "개")
        return f(*args)
    return ret_func


@mydecorator
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



'''
def mydecorator(f):
    def ret_func(*args):
        return f(*args)
    return ret_func
'''
# 데코레이터 기본 구조
