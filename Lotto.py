import random

pick = set()
while len(pick) < 6 :
    n = random.randint(1, 45)
    pick.add(n)

print(pick)
print(sorted(pick))

Lpick = []
while len(Lpick) < 6 :
    n = random.randint(1, 45)
    if n not in Lpick :
        Lpick.append(n)

print(pick)
print(sorted(pick))
