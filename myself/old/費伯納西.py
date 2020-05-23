cache=[0, 1, 1] + [None]*10
def fib(n):
  if cache[n]:
    return cache[n]
  cache[n] = fib(n-1) + fib(n-2)
  return cache[n]
  





print(fib(7))
