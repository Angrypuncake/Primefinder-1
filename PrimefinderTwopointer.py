def prime_finder(n):
#This is an overly complicated method of finding prime numbers by using double pointers in a list and nested while loops.

#Create a list comprehension of numbers using range(2,n) given that each element is not divisible by 2 so we're only dealing with a list of odd numbers.

  primes = [x for x in range(2,n + 1) if x > 2 and x % 2 != 0]
  

#Create a leftpointer set to start of list at index 0, create a right pointer starting at an index of 1
  left_pointer = 0 
  right_pointer = 1
  print("Unfiltered list: {0} \n".format(primes))
  removal_count = 0 

  print("...Starting filter...")
  while right_pointer <= len(primes) - 1:
    left_pointer = 0 
    while left_pointer < right_pointer:
  #if ele at right pointer is div by element at leftpointer, then list.remove(element) and use continue to repeat the conditional.
      print("Currently checking {0} with {1}".format(primes[right_pointer],primes[left_pointer]))
      if primes[right_pointer] % primes[left_pointer] == 0:
        print("{0} is divisible by {1}".format(primes[right_pointer], primes[left_pointer]))
        print("Removing %d" %(primes[right_pointer]))
        primes.remove(primes[right_pointer])
        left_pointer = 0
        removal_count += 1
        print("Removal count: {0}, new length: {1}".format(removal_count, len(primes) - 1 ))
        if right_pointer > len(primes) - 1:
          break
        continue
#increment leftpointer by one to shift it to the right to check the same element with a different number.
      left_pointer += 1
#The if statement below is to handle out of list index errors because everytime you remove an element, the list shortens by 1. For the final case, you would have the right_pointer < len(list) which generates an index error.
    print("{0} is prime".format(primes[right_pointer]))
    if right_pointer > len(primes) - 1:
      break
#When left pointer reaches right pointer, the current element is not divisible by any numbers before it and therefore can stay in the list, breaking the inner while loop. Increment right pointer by one to view next element. 
    right_pointer += 1 
  
  primes.insert(0,2)
#This part reintroduces 2 as a prime number into the list, this kinda feels like hard coding so maybe in a fixed version, I would leave 2 in when creating the list so I don't have to add it in later
  return primes



print(prime_finder(30))
#testing with n = 300

