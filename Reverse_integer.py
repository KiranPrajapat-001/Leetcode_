def reverse_int(x):
  rev = int(str(abs(x))[::-1]) 

  if x<0:
      rev = -rev
  return rev


x = int(input("Enter a number to be reversed:"))
Reversed_number = reverse_int(x)
print(Reversed_number)
        