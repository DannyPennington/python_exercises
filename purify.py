def purify(n):
  new = []
  for i in n:
    if i%2==0:
      new.append(i)
  return new

print (purify([1,2,3]))