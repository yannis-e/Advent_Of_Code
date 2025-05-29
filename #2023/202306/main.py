w = 0
for y in range(53916768):
    if y * (53916768 - y) > 250133010811025:
        w += 1
print(w)