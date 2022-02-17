from json.encoder import INFINITY
import random
from collections import Counter
from xmlrpc.client import MAXINT

nums = [] # type: list[int]
rand = MAXINT

for n in range(0, rand):
    b = random.randint(0, 5)
    nums.append(b)
    print(f"{n / rand * 100}%")

counter = Counter(nums);

for n in range(0, 6):
    occurrences = counter.get(n) or 0
    p = occurrences / rand * 100
    print(f"{n}: {p}%")
