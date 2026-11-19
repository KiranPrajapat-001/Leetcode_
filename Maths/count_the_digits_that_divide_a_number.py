def countDigit(num):
  count = 0
  number = str(num)
  for i in number:
    if num%int(i)==0:
      count+=1
  return count

num = int(input("Enter a Number: "))
print(countDigit(num))