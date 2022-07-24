import numpy as np

n=int(input())
trial=int(input())

list = []
for i in range(trial):
    x = np.random.randint(low=0, high=n)
    if x not in list:

        list.append(np.random.randint(low=0, high=n))

    else: break

print(list)
