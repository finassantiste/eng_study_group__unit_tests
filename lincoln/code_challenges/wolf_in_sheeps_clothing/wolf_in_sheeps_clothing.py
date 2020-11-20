# https://www.codewars.com/kata/5c8bfa44b9d1192e1ebd3d15
# (See screenshot in same folder.)


def warn_the_sheep(sheep_wolf_queue=None):
    if type(sheep_wolf_queue) is list:
        if sheep_wolf_queue[-1] == 'wolf':
            return 'Pls go away and stop eating my sheep'
        else:
            index = sheep_wolf_queue.index('wolf')
            length = len(sheep_wolf_queue)
            return f'Oi! Sheep number {length - index-1}! You are about to be eaten by a wolf!'
    else:
        return "sheep_wolf_queue is not a list"