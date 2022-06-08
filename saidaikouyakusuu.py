a = int(input("a?:"))
b = int(input("b?:"))
if a < b:
  e = a
else:
  e = b
gcd = 1
for i in range(2,e+1):
  if a%i==0 and b%i==0:
    gcd = i
print(str(gcd))
