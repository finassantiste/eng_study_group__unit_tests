# https://www.codewars.com/kata/5c8bfa44b9d1192e1ebd3d15
# (See screenshot in same folder.)


def warn_the_sheep(sheep_wolf_queue):
    wolf_sentece = 'Pls go away'
    wolf_name = 'wolf'
    save_sheep_sentence = "Oi! Sheep {}, wolf is behind you!"

    if sheep_wolf_queue[-1] == wolf_name:
        return wolf_sentece
    else:
        wolf_index = sheep_wolf_queue.index(wolf_name)
        sheep_position = len(sheep_wolf_queue) - wolf_index - 1

        return save_sheep_sentence.format(sheep_position)
