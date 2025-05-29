with open('day-4/input.txt', 'r') as f:
    data = f.read().splitlines()

t = 0

for i, x in enumerate(data):
    gs = x.strip().split(": ")[1].split(" | ")
    gs[0] = gs[0].split(" ")
    gs[1] = gs[1].split(" ")
    c = 0
    for n in gs[0]:
        for nu in gs[1]:
            if nu == n and nu != "":
                if c == 0:
                    c = 1
                else:
                    c = c * 2
    t = t + c

print(t)