smallest= None

nums = [1,2,3,4,5,6,453,566]

for num in nums:
  if smallest is None:
    smallest=num
  elif smallest<smallest:
    smallest=num
  print(num,smallest)
print("the smallest is",smallest)
