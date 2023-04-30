default_smallest = -1
nums = [1,2,3,4,5,6,453,566]
for i in nums:
  if i>default_smallest:
    default_smallest=i
  print(default_smallest,i)    
print(default_smallest)  
    
