import sys
from collections import deque, OrderedDict, defaultdict


def read_input(filename):
    with open(filename, "r") as f:
        tokens = f.read().strip().split()

    if len(tokens) < 2:
        raise ValueError("Input file must contain at least k and m.")

    k = int(tokens[0])
    m = int(tokens[1])
    requests = list(map(int, tokens[2:]))

    if k < 1:
        raise ValueError("Cache capacity k must be at least 1.")
    if len(requests) != m:
        raise ValueError(f"Expected {m} requests, but found {len(requests)}.")

    return k, m, requests

def main():
    if len(sys.argv) != 2:
        print(f"Usage: python {sys.argv[0]} <input_file>")
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
