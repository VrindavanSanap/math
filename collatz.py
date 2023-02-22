#https://www.youtube.com/watch?v=5mFpVDpKX70

def collatz(n):
  assert n!= 0
  list = []
  while n!= 1:
    if n%2==0:
      n = n//2
    else:
      n = 3*n + 1
    list.append(n)
  return list

print(collatz(7))
    
