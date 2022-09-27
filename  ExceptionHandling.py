import numpy

a = 5
b = 2


try:
     print("resource open")
     print(a/b)
     k = int(input("Enter a number"))
     print(k)

except ZeroDvisionError as e:
     print("Hey, You cannot didvide a Number by Zero", e
           )

except ValueError as e:
    print("invalid Input")


except Exception as e:
    print("Something waent Wrong.......")

finally:
    print("resource closed")
    
