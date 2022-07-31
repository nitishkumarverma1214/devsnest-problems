from re import X


def move_x_to_end(string):
    if len(string) ==1:
        return string

    res = move_x_to_end(string[1:])
    if string[0]=='x':
        return res+"x"
    else :
        return string[0]+res


print(move_x_to_end("axxbdxcefxhix"))