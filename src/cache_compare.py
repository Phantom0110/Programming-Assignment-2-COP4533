import sys
from collections import deque, OrderedDict, defaultdict


def read_input(filename):
    with open(filename, "r") as f:
        tokens = f.read().strip().split()

    k = int(tokens[0])
    m = int(tokens[1])
    requests = list(map(int, tokens[2:]))

    return k, m, requests


def fifo_misses(k, requests):

    cache = set()
    order = deque()
    misses = 0

    for item in requests:

        if item in cache:
            continue

        misses += 1

        if len(cache) < k:
            cache.add(item)
            order.append(item)

        else:
            evicted = order.popleft()
            cache.remove(evicted)

            cache.add(item)
            order.append(item)

    return misses


def lru_misses(k, requests):

    cache = OrderedDict()
    misses = 0

    for item in requests:

        if item in cache:
            cache.move_to_end(item)

        else:
            misses += 1

            if len(cache) == k:
                cache.popitem(last=False)

            cache[item] = True

    return misses


def optff_misses(k, requests):

    future = defaultdict(deque)

    for i, item in enumerate(requests):
        future[item].append(i)

    cache = set()
    misses = 0

    for i, item in enumerate(requests):

        future[item].popleft()

        if item in cache:
            continue

        misses += 1

        if len(cache) < k:
            cache.add(item)
            continue

        victim = None
        farthest = -1

        for c in cache:

            if not future[c]:
                victim = c
                break

            next_use = future[c][0]

            if next_use > farthest:
                farthest = next_use
                victim = c

        cache.remove(victim)
        cache.add(item)

    return misses


def main():

    if len(sys.argv) != 2:
        print("Usage: python cache_compare.py <input_file>")
        sys.exit(1)

    input_file = sys.argv[1]
    k, m, requests = read_input(input_file)

    fifo = fifo_misses(k, requests)
    lru = lru_misses(k, requests)
    optff = optff_misses(k, requests)

    print(f"FIFO  : {fifo}")
    print(f"LRU   : {lru}")
    print(f"OPTFF : {optff}")


if __name__ == "__main__":
    main()
