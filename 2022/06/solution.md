# Day 6

```
raw ← ⊃⎕NGET'/Users/mac/Desktop/random/adventofcode/2022/06/input.txt'1
utf8←'UTF-8'∘⎕ucs

⍝ --- part 1 ---
unique ← {(≢⍵) = 4}¨(4∪/(utf8 ⊃raw))
⊃(unique / ⍳≢unique) + 3

⍝ --- part 2 ---
unique ← {(≢⍵) = 14}¨(14∪/(utf8 ⊃raw))
⊃(unique / ⍳≢unique) + 13
```