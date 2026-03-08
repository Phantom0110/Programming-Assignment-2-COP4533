# Cache Eviction Policy Comparison

## Student Information
- Name: Mohammed Ali
- UFID: 39201267

## Language
This project is implemented in Python 3.

## Files
- `src/cache_compare.py` : main program
- `data/example.in` : example input
- `data/example.out` : expected output for example input

## Assumptions
- Input format is:
  - first line: `k m`
  - second line: `r1 r2 r3 ... rm`
- `k >= 1`
- requests are integers
- the number of requests provided equals `m`

## How to Run
From the repository root:

```bash
python3 src/cache_compare.py data/example.in
```
## Written Portion

Question 1: Empirical Comparison

The following table shows the number of misses for each cache policy on three input files with at least 50 requests each.

Input File	k	m	FIFO	LRU	OPTFF
file1.in	3	60	45	50	31
file2.in	4	56	44	48	23
file3.in	5	64	52	56	23

For all three files, OPTFF had the fewest misses. This makes sense because OPTFF is the optimal offline algorithm and uses knowledge of the full future request sequence.

For these test cases, FIFO also performed better than LRU. Even though LRU is often considered smarter than FIFO, it can still do worse on certain sequences. These results show that both FIFO and LRU depend on the request pattern, while OPTFF consistently gives the best possible result.

Question 2: Bad Sequence for LRU or FIFO

For k = 3, there does exist a request sequence for which OPTFF incurs strictly fewer misses than FIFO and LRU.

One such sequence is:

1 2 3 4 1 2 5 1 2 3 4 5
Miss Counts

For this sequence with cache size k = 3:

FIFO = 9 misses

LRU = 10 misses

OPTFF = 7 misses

Conclusion

So yes, such a sequence exists. In this example, OPTFF has strictly fewer misses than both FIFO and LRU.

Reasoning

FIFO evicts the page that has been in the cache the longest, without considering whether it will be needed again soon. LRU evicts the page whose most recent use was farthest in the past, but it also does not know the future. OPTFF, on the other hand, knows the full request sequence and evicts the page whose next use is farthest in the future.

Because of this extra future knowledge, OPTFF can make better eviction choices.

Question 3: Prove OPTFF is Optimal

We prove that OPTFF (Belady’s Farthest-in-Future algorithm) is optimal using an exchange argument.

Assume there is some other offline algorithm \(A\) that knows the full request sequence. Suppose \(A\) makes a different eviction choice than OPTFF at some point. Before that moment, both algorithms must have the same cache contents.

When the cache is full and a miss occurs, OPTFF evicts the page whose next use is farthest in the future (or never used again). Suppose OPTFF evicts page \(x\), but algorithm \(A\) evicts page \(y\).

Since OPTFF chose \(x\), that means \(y\) will be used again sooner than \(x\). Keeping \(y\) in the cache is therefore at least as good as keeping \(x\).

So we can modify algorithm \(A\) to evict \(x\) instead of \(y\) without increasing the number of misses. Repeating this process whenever \(A\) differs from OPTFF eventually turns \(A\) into OPTFF without making it worse.

Therefore, no algorithm can have fewer misses than OPTFF, which means **OPTFF is optimal**.
