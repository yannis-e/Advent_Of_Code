import re

with open('day-1\\input.txt', 'r') as f:
    data = f.read().splitlines()

t = 0

n = "one two three four five six seven eight nine".split()

p = "(?=(" + "|".join(n) + "|\\d))"

def f(x):
    if x in n:
        return str(n.index(x) + 1)
    return x

for x in data:
    didgets = [*map(f, re.findall(p, x))]
    t += int(didgets[0] + didgets[-1])

print(t)
