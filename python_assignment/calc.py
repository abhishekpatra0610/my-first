print("1.addition")
print("2.subtrsction")
print("3.multiplication")
print("4.division")

choice  = int(input("enter choice:"))
b = float(input("enter first number: "))
c =  float(input("enter second number: "))
  
if choice == 1:
  print("result =",b+c)

elif choice == 2:
  print("result =",b-c)

elif choice == 3:
  print("result =",b*c)

elif choice == 4:
  if c != 0:
   print("result =",b/c)
  else:
   print ("division by zero is not allowed")

else:
  print("invalid choice")
 

   
