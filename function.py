def simple_interest():
      global i
      p = float(input("enter the amount of principal amount"))
      n = int(input("enter the number of years"))
      r = float(input("enter the rate of interest"))
      i = p*n*r
      return i

i = simple_interest()
print("simple interest is = ",i)
