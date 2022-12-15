# Day 4

```
raw ← ⊃⎕NGET'/Users/mac/Desktop/random/adventofcode/2022/04/input.txt'1
findOne ← {(⍵⍷⍺) × (⍳(≢⍺))}
split ← {(⍺[⍳((⍺ findOne ⍵)-1)]) (⍺[(⍳((≢⍺)-(⍺ findOne ⍵)))+(⍺ findOne ⍵)])}
parsed ← {{⍵}¨({(⍎¨(⍵ split '-'))}¨(⍵ split ','))}¨raw

⍝ --- part 1 ---
+/{(×/⊃(⍵[1]-⍵[2])) ≤ 0}¨parsed

⍝ --- part 2 ---
+/{(×/⊃(⍵[1]-⊂(⌽⊃⍵[2]))) ≤ 0}¨parsed
```