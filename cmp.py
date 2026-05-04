#!/usr/bin/python3 -B

def handle(x):
    L = []
    for line in open(x):
        if not " has cost " in line: continue
        [_, c] = line.split(" has cost ")
        L.append(int(c))
    return L

O = handle("original")
D = handle("detour")
assert(len(O) == len(D))

owins = 0
dwins = 0
for o, d in zip(O, D):
    print(f"o={o} vs d={d}")
    if o < d:
        print("   o win!")
        owins += 1
    elif o > d:
        print("   d win!")
        dwins += 1
    else:
        print("   tie!")

print(f"detour wins:{dwins}")
print(f"original wins:{owins}")
