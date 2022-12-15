# Day 3

```
raw ← ⊃⎕NGET'/Users/mac/Desktop/random/adventofcode/2022/03/input.txt'1
utf8←'UTF-8'∘⎕ucs
eval ← {((utf8 ⍵) - (58 × ((utf8 ⍵) > (utf8 'a') - 1))) - 38}
tally ← {+/{(eval ⍵)=⍳52}¨⍵}

⍝ --- part 1 ---
matches ← {(tally ⍵[⍳((≢⍵)÷2)])×(tally ⍵[((≢⍵)÷2) + ⍳((≢⍵)÷2)])}¨raw
+/{{+/(⍵ > 0) × ⍳(≢⍵)}¨⍵}¨matches

⍝ --- part 2 ---
matches2 ← ×/{tally ⍵}¨((((≢raw) ÷ 3) 3) ⍴ raw)
+/{{+/(⍵ > 0) × ⍳(≢⍵)}¨⍵}¨matches
```
