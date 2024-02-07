import random
l1 = ['A', 'B', 'C', 'D', 'A', 'A', 'C']
matched_indexes = []
i = 0
length = len(l1)
rnglist = []
for i in range(100):
    randomLetter = random.choice(l1)
    rnglist.append(randomLetter)
print(rnglist)
count = l1.count('A')
print(count)

# print(f'{s} is present in {l1} at indexes {matched_indexes}')