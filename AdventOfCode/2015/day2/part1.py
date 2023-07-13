def part1():
    result = 0
    for line in open('input.txt'):
        l, w, h = map(int, line.split('x'))
        area = 2*l*w + 2*w*h + 2*h*l
        slack = min(l*w, w*h, h*l)
        result += area + slack
    print(result)


if __name__ == '__main__':
    part1()
