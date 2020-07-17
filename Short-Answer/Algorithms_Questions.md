# Analysis of Algorithms

## Exercise I

Give an analysis of the running time of each snippet of
pseudocode with respect to the input size n of each of the following:

```python
a)  a = 0 #o(1)
    # o(n^3)
    while (a < n * n * n): 
      #o(1)
      a = a + n * n
```


```
b)  sum = 0 o(1)
    for i in range(n): o(n)
      j = 1 o(1)
      while j < n: o(logn)
        j *= 2 o(1)
        sum += 1 o(1)
```

```
c)  def bunnyEars(bunnies):
      if bunnies == 0: o(1)
        return 0 o(1)

      return 2 + bunnyEars(bunnies-1) o(n) (o(logn)?)
```

## Exercise II

Suppose that you have an n-story building and plenty of eggs. Suppose also that an egg gets broken if it is thrown off floor f or higher, and doesn't get broken if dropped off a floor less than floor f. Devise a strategy to determine the value of f such that the number of dropped + broken eggs is minimized.

Write out your proposed algorithm in plain English or pseudocode AND give the runtime complexity of your solution.
