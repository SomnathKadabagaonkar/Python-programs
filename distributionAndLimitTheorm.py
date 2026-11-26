import math

x = 5
mean = 5
std = 2

n=5
p=0.4
q=0.6


result2=(1/(std*math.sqrt(2*math.pi)))*math.exp(-((x-mean)**2)/(2*std)**2)

result1=(math.factorial(n)/math.factorial(x)*math.factorial(n-x))*(p**(x))*q**(n-x)

result3=(x-mean)/(std/math.sqrt(n))

print("Binomail Distrubutuion =",result1)
print("Normal Distribution =", result2)
print("Central limit Theorem =", result3)



