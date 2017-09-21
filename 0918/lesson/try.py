l = list('abcde')
d = dict(name='Lux', champion_type='Magician')

print('program start!')
try:
    print('before l[5]')
    d['Sona']
    l[5]
    print('after l[5]')
except IndexError:
    print('l[5] exception!')
except KeyError:
    print("d['Sona'] exception!")

print('program terminate')


while True:
    try :
        value = int(input("숫자입력: "))
        l[value]
        print(l[value])
    except IndexError:
        print('IndexError!')
    except ValueError:
        print('ValueError!')
    else:
        print('good')
    finally:
        print('finished')
        break

