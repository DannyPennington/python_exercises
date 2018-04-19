def count(sequence, item):
  sum = 0
  for n in sequence:
    if n == item:
      sum += 1
  return sum

print (count([1,2,1,1], 1))