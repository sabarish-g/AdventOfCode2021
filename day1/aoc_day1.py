def read_data():
    with open('./input.txt', 'r') as f:
        input = f.read().splitlines()
        input = [int(i) for i in input]
    return input

def main():
    inc_count = 0
    inc_sliding_count = 0
    i = 1
    j = 3
    data = read_data()
    print(len(data))
    while i < len(data):
        if data[i] > data[i-1]:
            inc_count += 1
        i += 1
    print('Part 1: Number of increases is {}'.format(inc_count))
    while j < len(data):
        if data[j-3] + data[j-2] + data[j-1] < data[j-2] + data[j-1] + data[j]:
            inc_sliding_count += 1
        j += 1
    print('Part 2: Number of increases is {}'.format(inc_sliding_count))


if __name__ == '__main__':
    main()