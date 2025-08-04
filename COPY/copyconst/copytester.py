a = [1, 2, 3]
b = a      # yahan `b` ko `a` ki reference mil gayi hai

b[0] = 100

print(a)  # Output: [100, 2, 3]
print(b)  # Output: [100, 2, 3]

#memory address check

print(id(a))    #shows ke aik hi list hai in the same place/location too and 'b' ne 'a' ka reference lya hai
print(id(b))     

#SHALLOW COPY
c=a.copy()      #c is new list create hoi hai content same hai but location different hogi

print(id(c))     