
def what_fruit(color):
    color = color.lowercase()
    if color == 'red':
        return 'apple'
    elif color == 'yellow':
        return 'banana'
    elif color == 'green':
        return 'melon'
    else:
        return 'I don\'t know'

result = what_fruit('red')


def what_fruit2(color):
    fruit_color_dict = {
            'red' : 'apple',
            'yellow' : 'banana'
            'green': 'melon'
            }
    return
