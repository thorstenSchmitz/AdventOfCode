def part1():
    with open("input.in") as f:
        data = f.read().strip()
        houses = set()
        houses.add((0, 0))
        pos = (0, 0)
        for c in data:
            if c == "^":
                pos = (pos[0], pos[1] + 1)
            elif c == "v":
                pos = (pos[0], pos[1] - 1)
            elif c == ">":
                pos = (pos[0] + 1, pos[1])
            elif c == "<":
                pos = (pos[0] - 1, pos[1])
            houses.add(pos)
        print(len(houses))

def update(pos, c):
    if c == "^":
        return (pos[0], pos[1] + 1)
    elif c == "v":
        return (pos[0], pos[1] - 1)
    elif c == ">":
        return (pos[0] + 1, pos[1])
    elif c == "<":
        return (pos[0] - 1, pos[1])

def part2():
    with open("input.in") as f:
        data = f.read().strip()
        houses = set()
        houses.add((0, 0))
        santa = (0, 0)
        robo = (0, 0)
        for i, c in enumerate(data):




def main():
    part1()
    part2()


if __name__ == "__main__":
    main()
