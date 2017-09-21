vacation = 7

if vacation >= 7:
    print('Good')
elif vacation >= 5:
    print('Normal')
else:
    print('Bad')

print('Good') if vacation >= 7 else print('Normal') if vacation>=5 else print('Bad')


index = 0
fruits = ['apple', 'banana', 'melon']
colors = ['red', 'yellow', 'green', 'purple']

for fruit in fruits:
    print('fruit(%s), color(%s)' % (fruit, colors[index]))
    index +=1


for x in range(0,7):
    for y in range(0,4):
        print('(%d, %d)' % (x,y))


print([(x,y) for x in range(0,7) for y in range(0,4)])


l = ['(%d, %d)' % (x, y) for x in range(7) for y in range(4)]
print(l)

l2 = [(x, y) for x in range(7) for y in range(4)]
print(l2)

'''3번문제'''
for x in range(7):
    for y in range(4):
        if x % 2 == 0:
            print((x,y))

l2 = [(x, y) for x in range(7) for y in range(4) if x % 2 == 0]
print(l2)


3000*500/2
result = 0
for x in range(1000,2000):
    if x % 2 == 1:
        result += x
print(result)

result = sum([x for x in range(1000, 2000) if x % 2 == 1])
print(result)
result = sum([x for x in range(1001,2000, 2)])
print(result)


l = ['%d * %d = %d' % (x, y, x*y) for x in range(2,10) for y in range(1, 10)]
print(l)

gugu_index = 2
list_index = 0
for item in l:
    if list_index % 9 == 0:
        print('== %s단 ==' % gugu_index)
        gugu_index += 1
    list_index += 1
    print(item)

for list_index, item in enumerate(l):
    if list_index % 9 == 0:
        print(' == %s ==' % gugu_index)
        gugu_index += 1
    print(item)




gugu_list = [
        { 
            'title': '%d단' % x,
            'items': ['%d * %d = %d' % (x, y, x*y) for y in range(1, 10)]
        }
        for x in range(2, 10)
]
print(gugu_list)

for gugu in gugu_list:
    print(gugu['title'])
    for item in gugu['items']:
        print(item)
    print('')


'''7번'''
result =[]
for  x in range(1, 100):
    if x % 7 == 0 or x % 9 == 0:
        result.append(x)

print(result)




result = [
        x for x in range(100) if x % 7 == 0 or x % 9 ==0
        ]
print(result)



def multiply(*args):
        if len(args) == 1:
            return args[0] ** 2
        if len(args) == 2:
            return args[0] * args[1]
print(multiply(10))
print(multiply(2,3))



def calling():
    print('call function!')
calling()

def execute_arg_function(f):
    f()
execute_arg_function(calling)



champion = 'Lux'
def show_global_champion():
    print('show_global_champion : {}'.format(champion))
show_global_champion()
print('print champion : {}'.format(champion))



champion = 'Lux'

def show_global_champion():
    print('show_global_champion : {}'.format(champion))
def change_global_champion():
    #print('before change_global_champion : {}'.format(champion))
    champion = 'Ahri'
    print('after change_global_champion : {}'.format(champion))

show_global_champion()
change_global_champion()


print('lol')

champion = 'Lux'
def change_global_champion():
    champion = 'Ahri'
    print('after change_global_champion : {}'.format(champion))
change_global_champion()
print('print global champion : {}'.format(champion))


champion = 'Lux'
def change_global_champion():
    global champion
    champion = 'Ahri'
    print('after change_global_champion : {}'.format(champion))
change_global_champion()
print('print global champion : {}'.format(champion))




