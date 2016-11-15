def do_nothing():
    print('TEST01')


do_nothing()

def agree():
    return False

if agree():
    print('TRUE')
else:
    print('FALSE')

def echo(anything):
    return anything + ' ' + anything

print(echo('これはテストです'))


def commentary(color):
    if color == 'red':
        return "It's a tomato."
    elif color == 'green':
        return "It's a green pepper."
    elif color == 'bee purple':
        return "i don't know it is, but only bees can see it."
    else:
        return "I've never beard of the color " + color + "."

print(commentary('red'))
print(commentary('green'))
print(commentary('bee purple'))
print(commentary('blue'))



