# Day 2

```
raw ← ⊃⎕NGET'/Users/mac/Desktop/random/adventofcode/2022/02/input.txt'1
nums ← {(+/(⊢⍵[1]='ABBCCC')) (+/(⊢⍵[3]='XYYZZZ'))}¨raw

⍝ --- part 1 ---
+/{⍵[2] + 3×(3|(1 + -/⌽⍵))}¨nums

⍝ --- part 2 ---
+/{1 + (3×(⍵[2] - 1)) + (3|(+/⍵))}¨nums
```
