birthday={'naveen':'10-08-1997','siri':'15-12-1998','bin':'04-05-1999'}

while True:
	print("Enter name of your friend")
	name=input()
	if name=='':
		break
	if name in birthday:
		print(birthday[name]+'I have found')
	else:
		print("Enter the bday of new friend")
		bday=input()
		birthday[name]=bday
		print("Successfuly updated friends bday")
print(birthday)
		
