def addDigits(num):
  number = str(num)
  while len(number)>1:
    number = str(sum(int(digit) for digit in number))
  return int(number)

num = int(input("Enter a Number: "))
print(addDigits(num))