def collatz(number):
	if number%2==0:
		a=number/2
		print(a)
		return a
	elif number%2==1:
		b=(3*number+1)
		print(b)
		return b
print("Enter number:")
for i in range(1,6):
	
	x=int(input())
	collatz(x)
