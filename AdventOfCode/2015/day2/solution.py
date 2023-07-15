def part1():
    result = 0
    for line in open('input.txt'):
        l, w, h = map(int, line.split('x'))
        area = 2*l*w + 2*w*h + 2*h*l
        slack = min(l*w, w*h, h*l)
        result += area + slack
    print(result)


def part2():
    result = 0
    for line in open('input.txt'):
        sorting_line = sorted(map(int, line.split('x')))
        l, w, h = sorting_line[0], sorting_line[1], sorting_line[2]
        wrap = l + l + w + w
        bow = l*w*h
        result += wrap + bow
    print(result)


if __name__ == '__main__':
    part1()
    part2()
