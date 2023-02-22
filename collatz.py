#https://www.youtube.com/watch?v=5mFpVDpKX70

def collatz(n):
  if n < 1 or isinstance(n, int) == False:
     raise SyntaxError("collatz(): n must be a whole number")

  print(n)
  list = []
  while n!= 1:
    if n%2==0: n = n//2
    else: n = 3*n + 1
    list.append(n)
  return list

print(collatz(-1))
    
