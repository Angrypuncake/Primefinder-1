
def prime_finder(n):
  current_lst = [y for y in range(2,n + 1)]
  for x in range(2,n + 1):
      for i in range(2,x - 1):
        if x % i == 0 and x != 2:
          current_lst.remove(x)
          break 
  return(current_lst)

        

print(prime_finder(11))

