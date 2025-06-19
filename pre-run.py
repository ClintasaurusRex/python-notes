
def sum_of_digits(num):
  total = 0
  for digit in str(num):
    total += int(digit)
  print(total) 



def sum_of_digits(num):
  split = sum(int(d) for d in str(num))
  print(split)

sum_of_digits(123) # output = 6