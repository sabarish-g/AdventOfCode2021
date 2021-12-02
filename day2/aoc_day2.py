def read_data():
    with open('./input.txt', 'r') as f:
        data = f.read().splitlines()
    return data


def main():
    f = 0
    d = 0
    data = read_data()
    for command in data:
        comm = command.split(' ')[0]
        val = int(command.split(' ')[1])
        if comm == 'forward':
            f += val
        elif comm == 'down':
            d += val
        elif comm == 'up':
            d -= val
    print(f' Part 1: The final position is {f*d}')

    f2 = 0
    d2 = 0
    a = 0
    for command in data:
        comm = command.split(' ')[0]
        val = int(command.split(' ')[1])
        if comm == 'forward':
            f2 += val
            d2 = d2 + a*val
        elif comm == 'down':
            a += val
        elif comm == 'up':
            a -= val
    print(f' Part 2: The final position is {f2*d2}')


if __name__ == '__main__':
    main()
