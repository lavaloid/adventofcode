# Day 1

```
list ← (1000 2000 3000)(4000)(5000 6000)(7000 8000 9000)(10000)

⍝ --- part 1 ---
sums ← {+/⍵}¨list
⌈/sums

⍝ --- part 2 ---
rank ← ⍒sums
+/sums[rank[⍳3]]
```

For day 1 I cheated a bit and parsed the input using Python before running the code, because I couldn't figure out how to parse the input. Day 2 onwards will be fully in APL.
