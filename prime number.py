num = int(input("enter any number"))

i = 0
if num > 1:
      for j in range(2,num):
            if (num%j)==0:
                  i += 1
            else:
                  pass
if i>0:
      print(" not prime")
else:
      print("prime")
      
