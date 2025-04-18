import random
import struct
import sys

if len(sys.argv) != 2:
    print("Usage: python makePF.py <num_tuples>")
    sys.exit(1)

num_tuples = int(sys.argv[1])

if num_tuples <= 5:
    random_pairs = [(random.randint(0, 4), random.randint(0, 4)) for _ in range(num_tuples)]
else:
    random_pairs = [(random.randint(0, 9999), random.randint(0, 9999)) for _ in range(num_tuples)]

fn = 'tuple' + sys.argv[1] + '.bin'
with open(fn, 'wb') as f:
    for a, b in random_pairs:
        f.write(struct.pack('ii', a, b))
